"""
A scenic location is represented by its name and attractiveness score, where name is a unique string among all
locations and score is an integer. Locations can be ranked from the best to the worst.
The higher the score, the better the location. If the scores of two locations are equal,
then the location with the lexicographically smaller name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations.
It supports:

Adding scenic locations, one at a time.
Querying the ith best location of all locations already added, where i is the number of times the system has been
queried (including the current query).
For example, when the system is queried for the 4th time, it returns the 4th best location of all locations
already added.
Note that the test data are generated so that at any time, the number of queries does not exceed the number
of locations added to the system.

Implement the SORTracker class:

SORTracker() Initializes the tracker system.
void add(string name, int score) Adds a scenic location with name and score to the system.
string get() Queries and returns the ith best location, where i is the number of times this method has been invoked
(including this invocation).


Example 1:

Input
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
Output
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

Explanation
SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get();              // The sorted locations, from best to worst, are: branford, bradford.
                            // Note that branford precedes bradford due to its higher score (3 > 2).
                            // This is the 1st time get() is called, so return the best location: "branford".
tracker.add("alps", 2);     // Add location with name="alps" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford.
                            // Note that alps precedes bradford even though they have the same score (2).
                            // This is because "alps" is lexicographically smaller than "bradford".
                            // Return the 2nd best location "alps", as it is the 2nd time get() is called.
tracker.add("orland", 2);   // Add location with name="orland" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford, orland.
                            // Return "bradford", as it is the 3rd time get() is called.
tracker.add("orlando", 3);  // Add location with name="orlando" and score=3 to the system.
tracker.get();              // Sorted locations: branford, orlando, alps, bradford, orland.
                            // Return "bradford".
tracker.add("alpine", 2);   // Add location with name="alpine" and score=2 to the system.
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "bradford".
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "orland".

"""
from typing import List


"""Sorted List
==============
https://github.com/grantjenks/python-sortedcollections
"""
import sys
import traceback
from bisect import bisect_left, bisect_right, insort
from copy import deepcopy
from itertools import chain, repeat, starmap
from math import log
from operator import add, eq, ne, gt, ge, lt, le, iadd
from textwrap import dedent
try:
    from collections.abc import Sequence, MutableSequence
except ImportError:
    from collections import Sequence, MutableSequence
from functools import wraps
from functools import reduce
try:
    from _thread import get_ident
except ImportError:
    from _dummy_thread import get_ident
def recursive_repr(fillvalue='...'):
    def decorating_function(user_function):
        repr_running = set()
        @wraps(user_function)
        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result
        return wrapper
    return decorating_function
class SortedList(MutableSequence):
    DEFAULT_LOAD_FACTOR = 1000
    def __init__(self, iterable=None, key=None):
        assert key is None
        self._len = 0
        self._load = self.DEFAULT_LOAD_FACTOR
        self._lists = []
        self._maxes = []
        self._index = []
        self._offset = 0
        if iterable is not None:
            self._update(iterable)
    def __new__(cls, iterable=None, key=None):
        if key is None:
            return object.__new__(cls)
        else:
            if cls is SortedList:
                return object.__new__(SortedKeyList)
            else:
                raise TypeError('inherit SortedKeyList for key argument')
    @property
    def key(self):
        return None
    def _reset(self, load):
        values = reduce(iadd, self._lists, [])
        self._clear()
        self._load = load
        self._update(values)
    def clear(self):
        self._len = 0
        del self._lists[:]
        del self._maxes[:]
        del self._index[:]
        self._offset = 0
    _clear = clear
    def add(self, value):
        _lists = self._lists
        _maxes = self._maxes
        if _maxes:
            pos = bisect_right(_maxes, value)
            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _maxes[pos] = value
            else:
                insort(_lists[pos], value)
            self._expand(pos)
        else:
            _lists.append([value])
            _maxes.append(value)
        self._len += 1
    def _expand(self, pos):
        _load = self._load
        _lists = self._lists
        _index = self._index
        if len(_lists[pos]) > (_load << 1):
            _maxes = self._maxes
            _lists_pos = _lists[pos]
            half = _lists_pos[_load:]
            del _lists_pos[_load:]
            _maxes[pos] = _lists_pos[-1]
            _lists.insert(pos + 1, half)
            _maxes.insert(pos + 1, half[-1])
            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1
    def update(self, iterable):
        _lists = self._lists
        _maxes = self._maxes
        values = sorted(iterable)
        if _maxes:
            if len(values) * 4 >= self._len:
                _lists.append(values)
                values = reduce(iadd, _lists, [])
                values.sort()
                self._clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return
        _load = self._load
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _maxes.extend(sublist[-1] for sublist in _lists)
        self._len = len(values)
        del self._index[:]
    _update = update
    def __contains__(self, value):
        _maxes = self._maxes
        if not _maxes:
            return False
        pos = bisect_left(_maxes, value)
        if pos == len(_maxes):
            return False
        _lists = self._lists
        idx = bisect_left(_lists[pos], value)
        return _lists[pos][idx] == value
    def discard(self, value):
        _maxes = self._maxes
        if not _maxes:
            return
        pos = bisect_left(_maxes, value)
        if pos == len(_maxes):
            return
        _lists = self._lists
        idx = bisect_left(_lists[pos], value)
        if _lists[pos][idx] == value:
            self._delete(pos, idx)
    def remove(self, value):
        _maxes = self._maxes
        if not _maxes:
            raise ValueError('{0!r} not in list'.format(value))
        pos = bisect_left(_maxes, value)
        if pos == len(_maxes):
            raise ValueError('{0!r} not in list'.format(value))
        _lists = self._lists
        idx = bisect_left(_lists[pos], value)
        if _lists[pos][idx] == value:
            self._delete(pos, idx)
        else:
            raise ValueError('{0!r} not in list'.format(value))
    def _delete(self, pos, idx):
        _lists = self._lists
        _maxes = self._maxes
        _index = self._index
        _lists_pos = _lists[pos]
        del _lists_pos[idx]
        self._len -= 1
        len_lists_pos = len(_lists_pos)
        if len_lists_pos > (self._load >> 1):
            _maxes[pos] = _lists_pos[-1]
            if _index:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_lists) > 1:
            if not pos:
                pos += 1
            prev = pos - 1
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _lists[prev][-1]
            del _lists[pos]
            del _maxes[pos]
            del _index[:]
            self._expand(prev)
        elif len_lists_pos:
            _maxes[pos] = _lists_pos[-1]
        else:
            del _lists[pos]
            del _maxes[pos]
            del _index[:]
    def _loc(self, pos, idx):
        if not pos:
            return idx
        _index = self._index
        if not _index:
            self._build_index()
        total = 0
        pos += self._offset
        while pos:
            if not pos & 1:
                total += _index[pos - 1]
            pos = (pos - 1) >> 1
        return total + idx
    def _pos(self, idx):
        if idx < 0:
            last_len = len(self._lists[-1])
            if (-idx) <= last_len:
                return len(self._lists) - 1, last_len + idx
            idx += self._len
            if idx < 0:
                raise IndexError('list index out of range')
        elif idx >= self._len:
            raise IndexError('list index out of range')
        if idx < len(self._lists[0]):
            return 0, idx
        _index = self._index
        if not _index:
            self._build_index()
        pos = 0
        child = 1
        len_index = len(_index)
        while child < len_index:
            index_child = _index[child]
            if idx < index_child:
                pos = child
            else:
                idx -= index_child
                pos = child + 1
            child = (pos << 1) + 1
        return (pos - self._offset, idx)
    def _build_index(self):
        row0 = list(map(len, self._lists))
        if len(row0) == 1:
            self._index[:] = row0
            self._offset = 0
            return
        head = iter(row0)
        tail = iter(head)
        row1 = list(starmap(add, zip(head, tail)))
        if len(row0) & 1:
            row1.append(row0[-1])
        if len(row1) == 1:
            self._index[:] = row1 + row0
            self._offset = 1
            return
        size = 2 ** (int(log(len(row1) - 1, 2)) + 1)
        row1.extend(repeat(0, size - len(row1)))
        tree = [row0, row1]
        while len(tree[-1]) > 1:
            head = iter(tree[-1])
            tail = iter(head)
            row = list(starmap(add, zip(head, tail)))
            tree.append(row)
        reduce(iadd, reversed(tree), self._index)
        self._offset = size * 2 - 1
    def __delitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)
            if step == 1 and start < stop:
                if start == 0 and stop == self._len:
                    return self._clear()
                elif self._len <= 8 * (stop - start):
                    values = self._getitem(slice(None, start))
                    if stop < self._len:
                        values += self._getitem(slice(stop, None))
                    self._clear()
                    return self._update(values)
            indices = range(start, stop, step)
            if step > 0:
                indices = reversed(indices)
            _pos, _delete = self._pos, self._delete
            for index in indices:
                pos, idx = _pos(index)
                _delete(pos, idx)
        else:
            pos, idx = self._pos(index)
            self._delete(pos, idx)
    def __getitem__(self, index):
        _lists = self._lists
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)
            if step == 1 and start < stop:
                if start == 0 and stop == self._len:
                    return reduce(iadd, self._lists, [])
                start_pos, start_idx = self._pos(start)
                start_list = _lists[start_pos]
                stop_idx = start_idx + stop - start
                if len(start_list) >= stop_idx:
                    return start_list[start_idx:stop_idx]
                if stop == self._len:
                    stop_pos = len(_lists) - 1
                    stop_idx = len(_lists[stop_pos])
                else:
                    stop_pos, stop_idx = self._pos(stop)
                prefix = _lists[start_pos][start_idx:]
                middle = _lists[(start_pos + 1):stop_pos]
                result = reduce(iadd, middle, prefix)
                result += _lists[stop_pos][:stop_idx]
                return result
            if step == -1 and start > stop:
                result = self._getitem(slice(stop + 1, start + 1))
                result.reverse()
                return result
            indices = range(start, stop, step)
            return list(self._getitem(index) for index in indices)
        else:
            if self._len:
                if index == 0:
                    return _lists[0][0]
                elif index == -1:
                    return _lists[-1][-1]
            else:
                raise IndexError('list index out of range')
            if 0 <= index < len(_lists[0]):
                return _lists[0][index]
            len_last = len(_lists[-1])
            if -len_last < index < 0:
                return _lists[-1][len_last + index]
            pos, idx = self._pos(index)
            return _lists[pos][idx]
    _getitem = __getitem__
    def __setitem__(self, index, value):
        message = 'use ``del sl[index]`` and ``sl.add(value)`` instead'
        raise NotImplementedError(message)
    def __iter__(self):
        return chain.from_iterable(self._lists)
    def __reversed__(self):
        return chain.from_iterable(map(reversed, reversed(self._lists)))
    def reverse(self):
        raise NotImplementedError('use ``reversed(sl)`` instead')
    def islice(self, start=None, stop=None, reverse=False):
        _len = self._len
        if not _len:
            return iter(())
        start, stop, _ = slice(start, stop).indices(self._len)
        if start >= stop:
            return iter(())
        _pos = self._pos
        min_pos, min_idx = _pos(start)
        if stop == _len:
            max_pos = len(self._lists) - 1
            max_idx = len(self._lists[-1])
        else:
            max_pos, max_idx = _pos(stop)
        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)
    def _islice(self, min_pos, min_idx, max_pos, max_idx, reverse):
        _lists = self._lists
        if min_pos > max_pos:
            return iter(())
        if min_pos == max_pos:
            if reverse:
                indices = reversed(range(min_idx, max_idx))
                return map(_lists[min_pos].__getitem__, indices)
            indices = range(min_idx, max_idx)
            return map(_lists[min_pos].__getitem__, indices)
        next_pos = min_pos + 1
        if next_pos == max_pos:
            if reverse:
                min_indices = range(min_idx, len(_lists[min_pos]))
                max_indices = range(max_idx)
                return chain(
                    map(_lists[max_pos].__getitem__, reversed(max_indices)),
                    map(_lists[min_pos].__getitem__, reversed(min_indices)),
                )
            min_indices = range(min_idx, len(_lists[min_pos]))
            max_indices = range(max_idx)
            return chain(
                map(_lists[min_pos].__getitem__, min_indices),
                map(_lists[max_pos].__getitem__, max_indices),
            )
        if reverse:
            min_indices = range(min_idx, len(_lists[min_pos]))
            sublist_indices = range(next_pos, max_pos)
            sublists = map(_lists.__getitem__, reversed(sublist_indices))
            max_indices = range(max_idx)
            return chain(
                map(_lists[max_pos].__getitem__, reversed(max_indices)),
                chain.from_iterable(map(reversed, sublists)),
                map(_lists[min_pos].__getitem__, reversed(min_indices)),
            )
        min_indices = range(min_idx, len(_lists[min_pos]))
        sublist_indices = range(next_pos, max_pos)
        sublists = map(_lists.__getitem__, sublist_indices)
        max_indices = range(max_idx)
        return chain(
            map(_lists[min_pos].__getitem__, min_indices),
            chain.from_iterable(sublists),
            map(_lists[max_pos].__getitem__, max_indices),
        )
    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        _maxes = self._maxes
        if not _maxes:
            return iter(())
        _lists = self._lists
        if minimum is None:
            min_pos = 0
            min_idx = 0
        else:
            if inclusive[0]:
                min_pos = bisect_left(_maxes, minimum)
                if min_pos == len(_maxes):
                    return iter(())
                min_idx = bisect_left(_lists[min_pos], minimum)
            else:
                min_pos = bisect_right(_maxes, minimum)
                if min_pos == len(_maxes):
                    return iter(())
                min_idx = bisect_right(_lists[min_pos], minimum)
        if maximum is None:
            max_pos = len(_maxes) - 1
            max_idx = len(_lists[max_pos])
        else:
            if inclusive[1]:
                max_pos = bisect_right(_maxes, maximum)
                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_lists[max_pos])
                else:
                    max_idx = bisect_right(_lists[max_pos], maximum)
            else:
                max_pos = bisect_left(_maxes, maximum)
                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_lists[max_pos])
                else:
                    max_idx = bisect_left(_lists[max_pos], maximum)
        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)
    def __len__(self):
        return self._len
    def bisect_left(self, value):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos = bisect_left(_maxes, value)
        if pos == len(_maxes):
            return self._len
        idx = bisect_left(self._lists[pos], value)
        return self._loc(pos, idx)
    def bisect_right(self, value):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos = bisect_right(_maxes, value)
        if pos == len(_maxes):
            return self._len
        idx = bisect_right(self._lists[pos], value)
        return self._loc(pos, idx)
    bisect = bisect_right
    _bisect_right = bisect_right
    def count(self, value):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos_left = bisect_left(_maxes, value)
        if pos_left == len(_maxes):
            return 0
        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], value)
        pos_right = bisect_right(_maxes, value)
        if pos_right == len(_maxes):
            return self._len - self._loc(pos_left, idx_left)
        idx_right = bisect_right(_lists[pos_right], value)
        if pos_left == pos_right:
            return idx_right - idx_left
        right = self._loc(pos_right, idx_right)
        left = self._loc(pos_left, idx_left)
        return right - left
    def copy(self):
        return self.__class__(self)
    __copy__ = copy
    def append(self, value):
        raise NotImplementedError('use ``sl.add(value)`` instead')
    def extend(self, values):
        raise NotImplementedError('use ``sl.update(values)`` instead')
    def insert(self, index, value):
        raise NotImplementedError('use ``sl.add(value)`` instead')
    def pop(self, index=-1):
        if not self._len:
            raise IndexError('pop index out of range')
        _lists = self._lists
        if index == 0:
            val = _lists[0][0]
            self._delete(0, 0)
            return val
        if index == -1:
            pos = len(_lists) - 1
            loc = len(_lists[pos]) - 1
            val = _lists[pos][loc]
            self._delete(pos, loc)
            return val
        if 0 <= index < len(_lists[0]):
            val = _lists[0][index]
            self._delete(0, index)
            return val
        len_last = len(_lists[-1])
        if -len_last < index < 0:
            pos = len(_lists) - 1
            loc = len_last + index
            val = _lists[pos][loc]
            self._delete(pos, loc)
            return val
        pos, idx = self._pos(index)
        val = _lists[pos][idx]
        self._delete(pos, idx)
        return val
    def index(self, value, start=None, stop=None):
        _len = self._len
        if not _len:
            raise ValueError('{0!r} is not in list'.format(value))
        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0
        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len
        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))
        _maxes = self._maxes
        pos_left = bisect_left(_maxes, value)
        if pos_left == len(_maxes):
            raise ValueError('{0!r} is not in list'.format(value))
        _lists = self._lists
        idx_left = bisect_left(_lists[pos_left], value)
        if _lists[pos_left][idx_left] != value:
            raise ValueError('{0!r} is not in list'.format(value))
        stop -= 1
        left = self._loc(pos_left, idx_left)
        if start <= left:
            if left <= stop:
                return left
        else:
            right = self._bisect_right(value) - 1
            if start <= right:
                return start
        raise ValueError('{0!r} is not in list'.format(value))
    def __add__(self, other):
        values = reduce(iadd, self._lists, [])
        values.extend(other)
        return self.__class__(values)
    __radd__ = __add__
    def __iadd__(self, other):
        self._update(other)
        return self
    def __mul__(self, num):
        values = reduce(iadd, self._lists, []) * num
        return self.__class__(values)
    __rmul__ = __mul__
    def __imul__(self, num):
        values = reduce(iadd, self._lists, []) * num
        self._clear()
        self._update(values)
        return self
    def __make_cmp(seq_op, symbol, doc):
        def comparer(self, other):
            if not isinstance(other, Sequence):
                return NotImplemented
            self_len = self._len
            len_other = len(other)
            if self_len != len_other:
                if seq_op is eq:
                    return False
                if seq_op is ne:
                    return True
            for alpha, beta in zip(self, other):
                if alpha != beta:
                    return seq_op(alpha, beta)
            return seq_op(self_len, len_other)
        seq_op_name = seq_op.__name__
        comparer.__name__ = '__{0}__'.format(seq_op_name)
        doc_str = """Return true if and only if sorted list is {0} `other`.
        ``sl.__{1}__(other)`` <==> ``sl {2} other``
        Comparisons use lexicographical order as with sequences.
        Runtime complexity: `O(n)`
        :param other: `other` sequence
        :return: true if sorted list is {0} `other`
        """
        comparer.__doc__ = dedent(doc_str.format(doc, seq_op_name, symbol))
        return comparer
    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'less than')
    __gt__ = __make_cmp(gt, '>', 'greater than')
    __le__ = __make_cmp(le, '<=', 'less than or equal to')
    __ge__ = __make_cmp(ge, '>=', 'greater than or equal to')
    __make_cmp = staticmethod(__make_cmp)
    def __reduce__(self):
        values = reduce(iadd, self._lists, [])
        return (type(self), (values,))
    @recursive_repr()
    def __repr__(self):
        return '{0}({1!r})'.format(type(self).__name__, list(self))
    def _check(self):
        try:
            assert self._load >= 4
            assert len(self._maxes) == len(self._lists)
            assert self._len == sum(len(sublist) for sublist in self._lists)
            for sublist in self._lists:
                for pos in range(1, len(sublist)):
                    assert sublist[pos - 1] <= sublist[pos]
            for pos in range(1, len(self._lists)):
                assert self._lists[pos - 1][-1] <= self._lists[pos][0]
            for pos in range(len(self._maxes)):
                assert self._maxes[pos] == self._lists[pos][-1]
            double = self._load << 1
            assert all(len(sublist) <= double for sublist in self._lists)
            half = self._load >> 1
            for pos in range(0, len(self._lists) - 1):
                assert len(self._lists[pos]) >= half
            if self._index:
                assert self._len == self._index[0]
                assert len(self._index) == self._offset + len(self._lists)
                for pos in range(len(self._lists)):
                    leaf = self._index[self._offset + pos]
                    assert leaf == len(self._lists[pos])
                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if child >= len(self._index):
                        assert self._index[pos] == 0
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert child_sum == self._index[pos]
        except:
            traceback.print_exc(file=sys.stdout)
            print('len', self._len)
            print('load', self._load)
            print('offset', self._offset)
            print('len_index', len(self._index))
            print('index', self._index)
            print('len_maxes', len(self._maxes))
            print('maxes', self._maxes)
            print('len_lists', len(self._lists))
            print('lists', self._lists)
            raise
def identity(value):
    return value
class SortedKeyList(SortedList):
    def __init__(self, iterable=None, key=identity):
        self._key = key
        self._len = 0
        self._load = self.DEFAULT_LOAD_FACTOR
        self._lists = []
        self._keys = []
        self._maxes = []
        self._index = []
        self._offset = 0
        if iterable is not None:
            self._update(iterable)
    def __new__(cls, iterable=None, key=identity):
        return object.__new__(cls)
    @property
    def key(self):
        return self._key
    def clear(self):
        self._len = 0
        del self._lists[:]
        del self._keys[:]
        del self._maxes[:]
        del self._index[:]
    _clear = clear
    def add(self, value):
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        key = self._key(value)
        if _maxes:
            pos = bisect_right(_maxes, key)
            if pos == len(_maxes):
                pos -= 1
                _lists[pos].append(value)
                _keys[pos].append(key)
                _maxes[pos] = key
            else:
                idx = bisect_right(_keys[pos], key)
                _lists[pos].insert(idx, value)
                _keys[pos].insert(idx, key)
            self._expand(pos)
        else:
            _lists.append([value])
            _keys.append([key])
            _maxes.append(key)
        self._len += 1
    def _expand(self, pos):
        _lists = self._lists
        _keys = self._keys
        _index = self._index
        if len(_keys[pos]) > (self._load << 1):
            _maxes = self._maxes
            _load = self._load
            _lists_pos = _lists[pos]
            _keys_pos = _keys[pos]
            half = _lists_pos[_load:]
            half_keys = _keys_pos[_load:]
            del _lists_pos[_load:]
            del _keys_pos[_load:]
            _maxes[pos] = _keys_pos[-1]
            _lists.insert(pos + 1, half)
            _keys.insert(pos + 1, half_keys)
            _maxes.insert(pos + 1, half_keys[-1])
            del _index[:]
        else:
            if _index:
                child = self._offset + pos
                while child:
                    _index[child] += 1
                    child = (child - 1) >> 1
                _index[0] += 1
    def update(self, iterable):
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        values = sorted(iterable, key=self._key)
        if _maxes:
            if len(values) * 4 >= self._len:
                _lists.append(values)
                values = reduce(iadd, _lists, [])
                values.sort(key=self._key)
                self._clear()
            else:
                _add = self.add
                for val in values:
                    _add(val)
                return
        _load = self._load
        _lists.extend(values[pos:(pos + _load)]
                      for pos in range(0, len(values), _load))
        _keys.extend(list(map(self._key, _list)) for _list in _lists)
        _maxes.extend(sublist[-1] for sublist in _keys)
        self._len = len(values)
        del self._index[:]
    _update = update
    def __contains__(self, value):
        _maxes = self._maxes
        if not _maxes:
            return False
        key = self._key(value)
        pos = bisect_left(_maxes, key)
        if pos == len(_maxes):
            return False
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])
        while True:
            if _keys[pos][idx] != key:
                return False
            if _lists[pos][idx] == value:
                return True
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return False
                len_sublist = len(_keys[pos])
                idx = 0
    def discard(self, value):
        _maxes = self._maxes
        if not _maxes:
            return
        key = self._key(value)
        pos = bisect_left(_maxes, key)
        if pos == len(_maxes):
            return
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])
        while True:
            if _keys[pos][idx] != key:
                return
            if _lists[pos][idx] == value:
                self._delete(pos, idx)
                return
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return
                len_sublist = len(_keys[pos])
                idx = 0
    def remove(self, value):
        _maxes = self._maxes
        if not _maxes:
            raise ValueError('{0!r} not in list'.format(value))
        key = self._key(value)
        pos = bisect_left(_maxes, key)
        if pos == len(_maxes):
            raise ValueError('{0!r} not in list'.format(value))
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])
        while True:
            if _keys[pos][idx] != key:
                raise ValueError('{0!r} not in list'.format(value))
            if _lists[pos][idx] == value:
                self._delete(pos, idx)
                return
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    raise ValueError('{0!r} not in list'.format(value))
                len_sublist = len(_keys[pos])
                idx = 0
    def _delete(self, pos, idx):
        _lists = self._lists
        _keys = self._keys
        _maxes = self._maxes
        _index = self._index
        keys_pos = _keys[pos]
        lists_pos = _lists[pos]
        del keys_pos[idx]
        del lists_pos[idx]
        self._len -= 1
        len_keys_pos = len(keys_pos)
        if len_keys_pos > (self._load >> 1):
            _maxes[pos] = keys_pos[-1]
            if _index:
                child = self._offset + pos
                while child > 0:
                    _index[child] -= 1
                    child = (child - 1) >> 1
                _index[0] -= 1
        elif len(_keys) > 1:
            if not pos:
                pos += 1
            prev = pos - 1
            _keys[prev].extend(_keys[pos])
            _lists[prev].extend(_lists[pos])
            _maxes[prev] = _keys[prev][-1]
            del _lists[pos]
            del _keys[pos]
            del _maxes[pos]
            del _index[:]
            self._expand(prev)
        elif len_keys_pos:
            _maxes[pos] = keys_pos[-1]
        else:
            del _lists[pos]
            del _keys[pos]
            del _maxes[pos]
            del _index[:]
    def irange(self, minimum=None, maximum=None, inclusive=(True, True),
               reverse=False):
        min_key = self._key(minimum) if minimum is not None else None
        max_key = self._key(maximum) if maximum is not None else None
        return self._irange_key(
            min_key=min_key, max_key=max_key,
            inclusive=inclusive, reverse=reverse,
        )
    def irange_key(self, min_key=None, max_key=None, inclusive=(True, True),
                   reverse=False):
        _maxes = self._maxes
        if not _maxes:
            return iter(())
        _keys = self._keys
        if min_key is None:
            min_pos = 0
            min_idx = 0
        else:
            if inclusive[0]:
                min_pos = bisect_left(_maxes, min_key)
                if min_pos == len(_maxes):
                    return iter(())
                min_idx = bisect_left(_keys[min_pos], min_key)
            else:
                min_pos = bisect_right(_maxes, min_key)
                if min_pos == len(_maxes):
                    return iter(())
                min_idx = bisect_right(_keys[min_pos], min_key)
        if max_key is None:
            max_pos = len(_maxes) - 1
            max_idx = len(_keys[max_pos])
        else:
            if inclusive[1]:
                max_pos = bisect_right(_maxes, max_key)
                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_keys[max_pos])
                else:
                    max_idx = bisect_right(_keys[max_pos], max_key)
            else:
                max_pos = bisect_left(_maxes, max_key)
                if max_pos == len(_maxes):
                    max_pos -= 1
                    max_idx = len(_keys[max_pos])
                else:
                    max_idx = bisect_left(_keys[max_pos], max_key)
        return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)
    _irange_key = irange_key
    def bisect_left(self, value):
        return self._bisect_key_left(self._key(value))
    def bisect_right(self, value):
        return self._bisect_key_right(self._key(value))
    bisect = bisect_right
    def bisect_key_left(self, key):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos = bisect_left(_maxes, key)
        if pos == len(_maxes):
            return self._len
        idx = bisect_left(self._keys[pos], key)
        return self._loc(pos, idx)
    _bisect_key_left = bisect_key_left
    def bisect_key_right(self, key):
        _maxes = self._maxes
        if not _maxes:
            return 0
        pos = bisect_right(_maxes, key)
        if pos == len(_maxes):
            return self._len
        idx = bisect_right(self._keys[pos], key)
        return self._loc(pos, idx)
    bisect_key = bisect_key_right
    _bisect_key_right = bisect_key_right
    def count(self, value):
        _maxes = self._maxes
        if not _maxes:
            return 0
        key = self._key(value)
        pos = bisect_left(_maxes, key)
        if pos == len(_maxes):
            return 0
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        total = 0
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])
        while True:
            if _keys[pos][idx] != key:
                return total
            if _lists[pos][idx] == value:
                total += 1
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    return total
                len_sublist = len(_keys[pos])
                idx = 0
    def copy(self):
        return self.__class__(self, key=self._key)
    __copy__ = copy
    def index(self, value, start=None, stop=None):
        _len = self._len
        if not _len:
            raise ValueError('{0!r} is not in list'.format(value))
        if start is None:
            start = 0
        if start < 0:
            start += _len
        if start < 0:
            start = 0
        if stop is None:
            stop = _len
        if stop < 0:
            stop += _len
        if stop > _len:
            stop = _len
        if stop <= start:
            raise ValueError('{0!r} is not in list'.format(value))
        _maxes = self._maxes
        key = self._key(value)
        pos = bisect_left(_maxes, key)
        if pos == len(_maxes):
            raise ValueError('{0!r} is not in list'.format(value))
        stop -= 1
        _lists = self._lists
        _keys = self._keys
        idx = bisect_left(_keys[pos], key)
        len_keys = len(_keys)
        len_sublist = len(_keys[pos])
        while True:
            if _keys[pos][idx] != key:
                raise ValueError('{0!r} is not in list'.format(value))
            if _lists[pos][idx] == value:
                loc = self._loc(pos, idx)
                if start <= loc <= stop:
                    return loc
                elif loc > stop:
                    break
            idx += 1
            if idx == len_sublist:
                pos += 1
                if pos == len_keys:
                    raise ValueError('{0!r} is not in list'.format(value))
                len_sublist = len(_keys[pos])
                idx = 0
        raise ValueError('{0!r} is not in list'.format(value))
    def __add__(self, other):
        values = reduce(iadd, self._lists, [])
        values.extend(other)
        return self.__class__(values, key=self._key)
    __radd__ = __add__
    def __mul__(self, num):
        values = reduce(iadd, self._lists, []) * num
        return self.__class__(values, key=self._key)
    def __reduce__(self):
        values = reduce(iadd, self._lists, [])
        return (type(self), (values, self.key))
    @recursive_repr()
    def __repr__(self):
        type_name = type(self).__name__
        return '{0}({1!r}, key={2!r})'.format(type_name, list(self), self._key)
    def _check(self):
        try:
            assert self._load >= 4
            assert len(self._maxes) == len(self._lists) == len(self._keys)
            assert self._len == sum(len(sublist) for sublist in self._lists)
            for sublist in self._keys:
                for pos in range(1, len(sublist)):
                    assert sublist[pos - 1] <= sublist[pos]
            for pos in range(1, len(self._keys)):
                assert self._keys[pos - 1][-1] <= self._keys[pos][0]
            for val_sublist, key_sublist in zip(self._lists, self._keys):
                assert len(val_sublist) == len(key_sublist)
                for val, key in zip(val_sublist, key_sublist):
                    assert self._key(val) == key
            for pos in range(len(self._maxes)):
                assert self._maxes[pos] == self._keys[pos][-1]
            double = self._load << 1
            assert all(len(sublist) <= double for sublist in self._lists)
            half = self._load >> 1
            for pos in range(0, len(self._lists) - 1):
                assert len(self._lists[pos]) >= half
            if self._index:
                assert self._len == self._index[0]
                assert len(self._index) == self._offset + len(self._lists)
                for pos in range(len(self._lists)):
                    leaf = self._index[self._offset + pos]
                    assert leaf == len(self._lists[pos])
                for pos in range(self._offset):
                    child = (pos << 1) + 1
                    if child >= len(self._index):
                        assert self._index[pos] == 0
                    elif child + 1 == len(self._index):
                        assert self._index[pos] == self._index[child]
                    else:
                        child_sum = self._index[child] + self._index[child + 1]
                        assert child_sum == self._index[pos]
        except:
            traceback.print_exc(file=sys.stdout)
            print('len', self._len)
            print('load', self._load)
            print('offset', self._offset)
            print('len_index', len(self._index))
            print('index', self._index)
            print('len_maxes', len(self._maxes))
            print('maxes', self._maxes)
            print('len_keys', len(self._keys))
            print('keys', self._keys)
            print('len_lists', len(self._lists))
            print('lists', self._lists)
            raise
SortedListWithKey = SortedKeyList
"""Sorted Set
=============
https://github.com/grantjenks/python-sortedcontainers
"""
from itertools import chain
from operator import eq, ne, gt, ge, lt, le
from textwrap import dedent
try:
    from collections.abc import MutableSet, Sequence, Set
except ImportError:
    from collections import MutableSet, Sequence, Set
class SortedSet(MutableSet, Sequence):
    def __init__(self, iterable=None, key=None):
        self._key = key
        if not hasattr(self, '_set'):
            self._set = set()
        self._list = SortedList(self._set, key=key)
        _set = self._set
        self.isdisjoint = _set.isdisjoint
        self.issubset = _set.issubset
        self.issuperset = _set.issuperset
        _list = self._list
        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset
        if key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key
        if iterable is not None:
            self._update(iterable)
    @classmethod
    def _fromset(cls, values, key=None):
        sorted_set = object.__new__(cls)
        sorted_set._set = values
        sorted_set.__init__(key=key)
        return sorted_set
    @property
    def key(self):
        return self._key
    def __contains__(self, value):
        return value in self._set
    def __getitem__(self, index):
        return self._list[index]
    def __delitem__(self, index):
        _set = self._set
        _list = self._list
        if isinstance(index, slice):
            values = _list[index]
            _set.difference_update(values)
        else:
            value = _list[index]
            _set.remove(value)
        del _list[index]
    def __make_cmp(set_op, symbol, doc):
        def comparer(self, other):
            if isinstance(other, SortedSet):
                return set_op(self._set, other._set)
            elif isinstance(other, Set):
                return set_op(self._set, other)
            return NotImplemented
        set_op_name = set_op.__name__
        comparer.__name__ = '__{0}__'.format(set_op_name)
        doc_str = """Return true if and only if sorted set is {0} `other`.
        ``ss.__{1}__(other)`` <==> ``ss {2} other``
        Comparisons use subset and superset semantics as with sets.
        Runtime complexity: `O(n)`
        :param other: `other` set
        :return: true if sorted set is {0} `other`
        """
        comparer.__doc__ = dedent(doc_str.format(doc, set_op_name, symbol))
        return comparer
    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'a proper subset of')
    __gt__ = __make_cmp(gt, '>', 'a proper superset of')
    __le__ = __make_cmp(le, '<=', 'a subset of')
    __ge__ = __make_cmp(ge, '>=', 'a superset of')
    __make_cmp = staticmethod(__make_cmp)
    def __len__(self):
        return len(self._set)
    def __iter__(self):
        return iter(self._list)
    def __reversed__(self):
        return reversed(self._list)
    def add(self, value):
        _set = self._set
        if value not in _set:
            _set.add(value)
            self._list.add(value)
    _add = add
    def clear(self):
        self._set.clear()
        self._list.clear()
    def copy(self):
        return self._fromset(set(self._set), key=self._key)
    __copy__ = copy
    def count(self, value):
        return 1 if value in self._set else 0
    def discard(self, value):
        _set = self._set
        if value in _set:
            _set.remove(value)
            self._list.remove(value)
    _discard = discard
    def pop(self, index=-1):
        value = self._list.pop(index)
        self._set.remove(value)
        return value
    def remove(self, value):
        self._set.remove(value)
        self._list.remove(value)
    def difference(self, *iterables):
        diff = self._set.difference(*iterables)
        return self._fromset(diff, key=self._key)
    __sub__ = difference
    def difference_update(self, *iterables):
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _set.difference_update(values)
            _list.clear()
            _list.update(_set)
        else:
            _discard = self._discard
            for value in values:
                _discard(value)
        return self
    __isub__ = difference_update
    def intersection(self, *iterables):
        intersect = self._set.intersection(*iterables)
        return self._fromset(intersect, key=self._key)
    __and__ = intersection
    __rand__ = __and__
    def intersection_update(self, *iterables):
        _set = self._set
        _list = self._list
        _set.intersection_update(*iterables)
        _list.clear()
        _list.update(_set)
        return self
    __iand__ = intersection_update
    def symmetric_difference(self, other):
        diff = self._set.symmetric_difference(other)
        return self._fromset(diff, key=self._key)
    __xor__ = symmetric_difference
    __rxor__ = __xor__
    def symmetric_difference_update(self, other):
        _set = self._set
        _list = self._list
        _set.symmetric_difference_update(other)
        _list.clear()
        _list.update(_set)
        return self
    __ixor__ = symmetric_difference_update
    def union(self, *iterables):
        return self.__class__(chain(iter(self), *iterables), key=self._key)
    __or__ = union
    __ror__ = __or__
    def update(self, *iterables):
        _set = self._set
        _list = self._list
        values = set(chain(*iterables))
        if (4 * len(values)) > len(_set):
            _list = self._list
            _set.update(values)
            _list.clear()
            _list.update(_set)
        else:
            _add = self._add
            for value in values:
                _add(value)
        return self
    __ior__ = update
    _update = update
    def __reduce__(self):
        return (type(self), (self._set, self._key))
    @recursive_repr()
    def __repr__(self):
        _key = self._key
        key = '' if _key is None else ', key={0!r}'.format(_key)
        type_name = type(self).__name__
        return '{0}({1!r}{2})'.format(type_name, list(self), key)
    def _check(self):
        _set = self._set
        _list = self._list
        _list._check()
        assert len(_set) == len(_list)
        assert all(value in _set for value in _list)
"""Sorted Dict
==============
https://github.com/grantjenks/python-sortedcontainers
"""
import sys
import warnings
from itertools import chain
try:
    from collections.abc import (
        ItemsView, KeysView, Mapping, ValuesView, Sequence
    )
except ImportError:
    from collections import ItemsView, KeysView, Mapping, ValuesView, Sequence
class SortedDict(dict):
    def __init__(self, *args, **kwargs):
        if args and (args[0] is None or callable(args[0])):
            _key = self._key = args[0]
            args = args[1:]
        else:
            _key = self._key = None
        self._list = SortedList(key=_key)
        _list = self._list
        self._list_add = _list.add
        self._list_clear = _list.clear
        self._list_iter = _list.__iter__
        self._list_reversed = _list.__reversed__
        self._list_pop = _list.pop
        self._list_remove = _list.remove
        self._list_update = _list.update
        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect_right
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset
        if _key is not None:
            self.bisect_key_left = _list.bisect_key_left
            self.bisect_key_right = _list.bisect_key_right
            self.bisect_key = _list.bisect_key
            self.irange_key = _list.irange_key
        self._update(*args, **kwargs)
    @property
    def key(self):
        return self._key
    @property
    def iloc(self):
        try:
            return self._iloc
        except AttributeError:
            warnings.warn(
                'sorted_dict.iloc is deprecated.'
                ' Use SortedDict.keys() instead.',
                DeprecationWarning,
                stacklevel=2,
            )
            _iloc = self._iloc = SortedKeysView(self)
            return _iloc
    def clear(self):
        dict.clear(self)
        self._list_clear()
    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._list_remove(key)
    def __iter__(self):
        return self._list_iter()
    def __reversed__(self):
        return self._list_reversed()
    def __setitem__(self, key, value):
        if key not in self:
            self._list_add(key)
        dict.__setitem__(self, key, value)
    _setitem = __setitem__
    def __or__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(self.items(), other.items())
        return self.__class__(self._key, items)
    def __ror__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        items = chain(other.items(), self.items())
        return self.__class__(self._key, items)
    def __ior__(self, other):
        self._update(other)
        return self
    def copy(self):
        return self.__class__(self._key, self.items())
    __copy__ = copy
    @classmethod
    def fromkeys(cls, iterable, value=None):
        return cls((key, value) for key in iterable)
    def keys(self):
        return SortedKeysView(self)
    def items(self):
        return SortedItemsView(self)
    def values(self):
        return SortedValuesView(self)
    if sys.hexversion < 0x03000000:
        def __make_raise_attributeerror(original, alternate):
            # pylint: disable=no-self-argument
            message = (
                'SortedDict.{original}() is not implemented.'
                ' Use SortedDict.{alternate}() instead.'
            ).format(original=original, alternate=alternate)
            def method(self):
                # pylint: disable=missing-docstring,unused-argument
                raise AttributeError(message)
            method.__name__ = original  # pylint: disable=non-str-assignment-to-dunder-name
            method.__doc__ = message
            return property(method)
        iteritems = __make_raise_attributeerror('iteritems', 'items')
        iterkeys = __make_raise_attributeerror('iterkeys', 'keys')
        itervalues = __make_raise_attributeerror('itervalues', 'values')
        viewitems = __make_raise_attributeerror('viewitems', 'items')
        viewkeys = __make_raise_attributeerror('viewkeys', 'keys')
        viewvalues = __make_raise_attributeerror('viewvalues', 'values')
    class _NotGiven(object):
        # pylint: disable=too-few-public-methods
        def __repr__(self):
            return '<not-given>'
    __not_given = _NotGiven()
    def pop(self, key, default=__not_given):
        if key in self:
            self._list_remove(key)
            return dict.pop(self, key)
        else:
            if default is self.__not_given:
                raise KeyError(key)
            return default
    def popitem(self, index=-1):
        if not self:
            raise KeyError('popitem(): dictionary is empty')
        key = self._list_pop(index)
        value = dict.pop(self, key)
        return (key, value)
    def peekitem(self, index=-1):
        key = self._list[index]
        return key, self[key]
    def setdefault(self, key, default=None):
        if key in self:
            return self[key]
        dict.__setitem__(self, key, default)
        self._list_add(key)
        return default
    def update(self, *args, **kwargs):
        if not self:
            dict.update(self, *args, **kwargs)
            self._list_update(dict.__iter__(self))
            return
        if not kwargs and len(args) == 1 and isinstance(args[0], dict):
            pairs = args[0]
        else:
            pairs = dict(*args, **kwargs)
        if (10 * len(pairs)) > len(self):
            dict.update(self, pairs)
            self._list_clear()
            self._list_update(dict.__iter__(self))
        else:
            for key in pairs:
                self._setitem(key, pairs[key])
    _update = update
    def __reduce__(self):
        items = dict.copy(self)
        return (type(self), (self._key, items))
    @recursive_repr()
    def __repr__(self):
        _key = self._key
        type_name = type(self).__name__
        key_arg = '' if _key is None else '{0!r}, '.format(_key)
        item_format = '{0!r}: {1!r}'.format
        items = ', '.join(item_format(key, self[key]) for key in self._list)
        return '{0}({1}{{{2}}})'.format(type_name, key_arg, items)
    def _check(self):
        _list = self._list
        _list._check()
        assert len(self) == len(_list)
        assert all(key in self for key in _list)
def _view_delitem(self, index):
    _mapping = self._mapping
    _list = _mapping._list
    dict_delitem = dict.__delitem__
    if isinstance(index, slice):
        keys = _list[index]
        del _list[index]
        for key in keys:
            dict_delitem(_mapping, key)
    else:
        key = _list.pop(index)
        dict_delitem(_mapping, key)
class SortedKeysView(KeysView, Sequence):
    __slots__ = ()
    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)
    def __getitem__(self, index):
        return self._mapping._list[index]
    __delitem__ = _view_delitem
class SortedItemsView(ItemsView, Sequence):
    __slots__ = ()
    @classmethod
    def _from_iterable(cls, it):
        return SortedSet(it)
    def __getitem__(self, index):
        _mapping = self._mapping
        _mapping_list = _mapping._list
        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [(key, _mapping[key]) for key in keys]
        key = _mapping_list[index]
        return key, _mapping[key]
    __delitem__ = _view_delitem
class SortedValuesView(ValuesView, Sequence):
    __slots__ = ()
    def __getitem__(self, index):
        _mapping = self._mapping
        _mapping_list = _mapping._list
        if isinstance(index, slice):
            keys = _mapping_list[index]
            return [_mapping[key] for key in keys]
        key = _mapping_list[index]
        return _mapping[key]
    __delitem__ = _view_delitem
class ItemSortedDict(SortedDict):
    def __init__(self, *args, **kwargs):
        assert args and callable(args[0])
        args = list(args)
        func = self._func = args[0]
        def key_func(key):
            return func(key, self[key])
        args[0] = key_func
        super().__init__(*args, **kwargs)
    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        self._list_remove(key)
        dict.__delitem__(self, key)
    def __setitem__(self, key, value):
        if key in self:
            self._list_remove(key)
            dict.__delitem__(self, key)
        dict.__setitem__(self, key, value)
        self._list_add(key)
    _setitem = __setitem__
    def copy(self):
        "Return shallow copy of the mapping."
        return self.__class__(self._func, iter(self.items()))
    __copy__ = copy
    def __deepcopy__(self, memo):
        items = (deepcopy(item, memo) for item in self.items())
        return self.__class__(self._func, items)


class SORTracker:

    def __init__(self):
        self.sd = ItemSortedDict(lambda k, v: (-v, k))
        self.i = 0

    def add(self, name: str, score: int) -> None:
        self.sd[name] = score

    def get(self) -> str:
        self.i += 1
        return self.sd.peekitem(self.i - 1)[0]


def main():
    tracker = SORTracker()
    print(tracker.add("bradford", 2))
    print(tracker.add("branford", 3))
    print(tracker.get())
    print(tracker.add("alps", 2))
    print(tracker.get())
    print(tracker.add("orland", 2))
    print(tracker.get())
    print(tracker.add("orlando", 3))
    print(tracker.get())
    print(tracker.add("alpine", 2))
    print(tracker.get())
    print(tracker.get())


if __name__ == '__main__':
    main()

"""
Design an iterator that supports the peek operation on an existing iterator
in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
int next() Returns the next element in the array and moves the pointer to the next element.
boolean hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
Note: Each language may have a different implementation of the constructor and Iterator,
but they all support the int next() and boolean hasNext() functions.



Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
All the calls to next and peek are valid.
At most 1000 calls will be made to next, hasNext, and peek.


Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.it = iter(nums)
        self.next_item = next(self.it)
        self.has_next = True

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.has_next

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        ans = self.next_item
        try:
            self.next_item = next(self.it)
        except StopIteration:
            self.has_next = False
        return ans


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_item = self.iterator.next()
        self.last = False
        self.has_next = True

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_item

    def next(self):
        """
        :rtype: int
        """
        ans = self.next_item
        self.next_item = self.iterator.next()
        if self.last and not self.iterator.hasNext():
            self.has_next = False
        self.last = not self.iterator.hasNext()
        return ans


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next


def main():
    iterator = Iterator([1, 2, 3, 4])
    peekingIterator = PeekingIterator(iterator)
    print(peekingIterator.hasNext())
    print(peekingIterator.peek())
    print(peekingIterator.peek())
    print(peekingIterator.next())
    print(peekingIterator.next())
    print(peekingIterator.peek())
    print(peekingIterator.peek())
    print(peekingIterator.next())
    print(peekingIterator.hasNext())
    print(peekingIterator.peek())
    print(peekingIterator.hasNext())
    print(peekingIterator.next())
    print(peekingIterator.hasNext())


if __name__ == '__main__':
    main()

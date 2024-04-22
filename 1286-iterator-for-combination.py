"""
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters
of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.


Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False


Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 104 calls will be made to next and hasNext.
It is guaranteed that all calls of the function next are valid.

"""
from collections import deque
from itertools import combinations
from typing import List


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = combinations(characters, combinationLength)
        self.q = deque()

    def next(self) -> str:
        if self.q:
            return self.q.popleft()
        return ''.join(next(self.c))

    def hasNext(self) -> bool:
        if self.q:
            return True
        try:
            self.q.append(''.join(next(self.c)))
        except StopIteration:
            return False
        return True


def main():
    itr = CombinationIterator("abc", 2)
    print(itr.next())
    print(itr.hasNext())
    print(itr.next())
    print(itr.hasNext())
    print(itr.next())
    print(itr.hasNext())


if __name__ == '__main__':
    main()

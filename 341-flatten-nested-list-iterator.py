"""
You are given a nested list of integers nestedList.
Each element is either an integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.



Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].


Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].
"""


class NestedInteger:
    def __init__(self, val):
        self.val = val

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.val, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if self.isInteger():
            return self.val

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        if not self.isInteger():
            return self.val


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.vals = self.traverse(nestedList)
        try:
            self.next_val = next(self.vals)
        except StopIteration:
            self.next_val = None

    def traverse(self, nestedList):
        for val in nestedList:
            if val.isInteger():
                yield val.getInteger()
            else:
                yield from self.traverse(val.getList())

    def next(self) -> int:
        val = self.next_val
        try:
            self.next_val = next(self.vals)
        except StopIteration:
            self.next_val = None
        return val

    def hasNext(self) -> bool:
        return self.next_val is not None


def main():
    nestedList = [NestedInteger(0)]
    # nestedList = [NestedInteger(1), NestedInteger(2), NestedInteger(3)]
    # nestedList = [NestedInteger([NestedInteger(1), NestedInteger(2)]),
    #               NestedInteger(3),
    #               NestedInteger([NestedInteger(4), NestedInteger(5)]),
    #               NestedInteger([NestedInteger(6), NestedInteger([NestedInteger(7)])])]
    # nestedList = [NestedInteger([NestedInteger([])])]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        # v.append(i.next())
        print(i.next())
    # print(v)

if __name__ == '__main__':
    main()

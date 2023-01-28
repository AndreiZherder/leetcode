"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list
of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals
[starti, endi]. The answer should be sorted by starti.


Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
"getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]],
null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]


Constraints:

0 <= value <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.


Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size
of the data stream?
"""
from typing import List
from sortedcontainers import SortedList


class SummaryRanges:

    def __init__(self):
        self.sl = SortedList()

    def merge(self, i: int, j: int) -> None:
        left = self.sl[i][0]
        right = self.sl[j][1]
        self.sl.pop(j)
        self.sl.pop(i)
        self.sl.add([left, right])

    def addNum(self, value: int) -> None:
        i = self.sl.bisect_right([value, 10001]) - 1
        if i != -1:
            if self.sl[i][1] == value - 1:
                self.sl[i][1] = value
                if i + 1 < len(self.sl) and self.sl[i][1] == self.sl[i + 1][0] - 1:
                    self.merge(i, i + 1)
            elif self.sl[i][1] < value - 1:
                if i + 1 < len(self.sl) and self.sl[i + 1][0] == value + 1:
                    self.sl[i + 1][0] -= 1
                else:
                    self.sl.add([value, value])
        else:
            if i + 1 < len(self.sl) and self.sl[i + 1][0] == value + 1:
                self.sl[i + 1][0] -= 1
            else:
                self.sl.add([value, value])

    def getIntervals(self) -> List[List[int]]:
        return list(self.sl)


def main():
    summaryRanges = SummaryRanges()
    print(summaryRanges.addNum(1))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(3))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(7))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(2))
    print(summaryRanges.getIntervals())
    print(summaryRanges.addNum(6))
    print(summaryRanges.getIntervals())


if __name__ == '__main__':
    main()

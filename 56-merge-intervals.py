"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cur_left, cur_right = intervals[0]
        for left, right in intervals[1:]:
            if left <= cur_right:
                cur_right = max(cur_right, right)
            else:
                ans.append([cur_left, cur_right])
                cur_left, cur_right = left, right
        ans.append([cur_left, cur_right])
        return ans


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))


if __name__ == '__main__':
    main()

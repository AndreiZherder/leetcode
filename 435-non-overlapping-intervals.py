"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

"""
from bisect import bisect_left
from functools import lru_cache
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            if i == n:
                return 0
            ans1 = 1 + dp(i + 1)
            j = bisect_left(starts, intervals[i][1])
            ans2 = j - i - 1 + dp(j)
            return min(ans1, ans2)

        n = len(intervals)
        intervals.sort()
        starts = [intervals[i][0] for i in range(n)]
        return dp(0)


def main():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(Solution().eraseOverlapIntervals(intervals))


if __name__ == '__main__':
    main()

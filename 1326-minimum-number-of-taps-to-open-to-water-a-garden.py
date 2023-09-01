"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n.
(i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means
the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden,
If the garden cannot be watered return -1.



Example 1:
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.


Constraints:

1 <= n <= 104
ranges.length == n + 1
0 <= ranges[i] <= 100
"""
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        def find_next(i: int) -> int:
            x1, x2 = intervals[i]
            best = x2
            besti = i
            i += 1
            while i < n + 1 and intervals[i][0] <= x2:
                if intervals[i][1] > best:
                    best = intervals[i][1]
                    besti = i
                i += 1
            return besti

        intervals = [[i - num, i + num] for i, num in enumerate(ranges)]
        intervals.append([-10 ** 20, 0])
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for x1, x2 in intervals:
            if x1 <= 0 and x2 >= n:
                return 1
        i = 0
        ans = 0
        while True:
            ni = find_next(i)
            if ni == i:
                return -1
            x1, x2 = intervals[ni]
            ans += 1
            if x2 >= n:
                return ans
            i = ni


def main():
    n = 19
    ranges = [4, 1, 5, 0, 5, 3, 3, 3, 0, 0, 3, 3, 2, 2, 4, 4, 2, 3, 4, 2]
    print(Solution().minTaps(n, ranges))


if __name__ == '__main__':
    main()

"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between
any two time-points in the list.


Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        a = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timePoints])
        best = 10 **20
        for i in range(1, n):
            best = min(best, a[i] - a[i - 1])
        best = min(best, (a[0] - a[-1]) % 1440)
        return best


def main():
    timePoints = ["00:00", "23:59", "00:00"]
    print(Solution().findMinDifference(timePoints))


if __name__ == '__main__':
    main()

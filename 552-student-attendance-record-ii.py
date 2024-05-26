"""
An attendance record for a student can be represented as a string where each character signifies whether the student
was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible
for an attendance award. The answer may be very large, so return it modulo 109 + 7.



Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316


Constraints:

1 <= n <= 105

"""
from functools import lru_cache
from typing import List


class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache(None)
        def dp(i: int, absent: int, late: int) -> int:
            if i == n:
                return 1
            ans = 0
            if not absent:
                ans = (ans + dp(i + 1, 1, 0)) % mod
            if late != 2:
                ans = (ans + dp(i + 1, absent, late + 1)) % mod
            ans = (ans + dp(i + 1, absent, 0)) % mod
            return ans
        mod = 10 ** 9 + 7
        ans = dp(0, 0, 0)
        dp.cache_clear()
        return ans


def main():
    n = 2
    print(Solution().checkRecord(n))


if __name__ == '__main__':
    main()

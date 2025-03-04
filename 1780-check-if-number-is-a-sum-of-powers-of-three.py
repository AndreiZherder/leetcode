"""
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three.
Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.



Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false


Constraints:

1 <= n <= 107

"""
from functools import lru_cache


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        @lru_cache(None)
        def dp(n: int, used: int) -> bool:
            if n == 0:
                return True
            cur = 1
            p = 0
            while cur <= n:
                if used & (1 << p) == 0 and dp(n - cur, used | 1 << p):
                    return True
                cur *= 3
                p += 1
            return False
        return dp(n, 0)


def main():
    n = 21
    print(Solution().checkPowersOfThree(n))


if __name__ == '__main__':
    main()

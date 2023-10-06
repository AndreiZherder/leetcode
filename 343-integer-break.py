"""
Given an integer n, break it into the sum of k positive integers, where k >= 2,
and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


Constraints:

2 <= n <= 58
"""
from functools import lru_cache
from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(n: int) -> int:
            if n == 1:
                return 1
            best = 0
            for i in range(1, n // 2 + 1):
                best = max(best, i * (n - i))
                best = max(best, dp(i) * (n - i))
                best = max(best, i * dp(n - i))
                best = max(best, dp(i) * dp(n - i))
            return best

        return dp(n)


def main():
    n = 10
    print(Solution().integerBreak(n))


if __name__ == '__main__':
    main()

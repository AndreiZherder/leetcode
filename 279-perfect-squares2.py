"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""
from functools import lru_cache
from math import sqrt



class Solution:
    def numSquares(self, n: int) -> int:
        @lru_cache(None)
        def dp(total: int) -> int:
            if total > n:
                return 10 ** 20
            if total == n:
                return 0
            ans = 10 ** 20
            for i in range(m):
                ans = min(ans, 1 + dp(total + xs[i]))
            return ans

        xs = []
        x = 1
        while x ** 2 <= n:
            xs.append(x ** 2)
            x += 1
        m = len(xs)
        return dp(0)


def main():
    n = 9999
    print(Solution().numSquares(n))


if __name__ == '__main__':
    main()

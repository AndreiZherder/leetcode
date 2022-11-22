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
from math import sqrt



class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(sqrt(n) + 1))]
        m = len(squares)
        dp = [float('Inf') for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(m):
                if i - squares[j] >= 0:
                    dp[i] = min(dp[i], dp[i - squares[j]] + 1)
        return dp[n]


def main():
    n = 9999
    print(Solution().numSquares(n))


if __name__ == '__main__':
    main()

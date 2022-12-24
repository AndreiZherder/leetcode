"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
Given an integer n, return the number of ways to tile an 2 x n board.
Since the answer may be very large, return it modulo 10^9 + 7.

In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
such that exactly one of the tilings has both squares occupied by a tile.



Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 1000
"""


class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0, 0, 1] + [0 for i in range(n)]
        tromino_total = 0
        for i in range(3, n + 3):
            dp[i] = (dp[i - 1] + dp[i - 2] + tromino_total) % mod
            tromino_total = (tromino_total + dp[i - 2] * 2) % mod
        return dp[-1]


def main():
    n = 4
    print(Solution().numTilings(n))


if __name__ == '__main__':
    main()

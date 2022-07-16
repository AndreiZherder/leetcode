"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid
crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn,
return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12


Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def inside(i: int, j: int) -> bool:
            return 1 <= i <= m and 1 <= j <= n

        p = 10 ** 9 + 7
        dp = [[[0 for j in range(n + 2)] for i in range(m + 2)] for k in range(maxMove + 1)]
        dp[0][startRow + 1][startColumn + 1] = 1
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for k in range(1, maxMove + 1):
            for i in range(m + 2):
                for j in range(n + 2):
                    for di, dj in moves:
                        if inside(i + di, j + dj):
                            dp[k][i][j] = (dp[k][i][j] + dp[k - 1][i + di][j + dj]) % p
        ans = 0
        for k in range(maxMove + 1):
            for i in [0, m + 1]:
                for j in range(1, n + 1):
                    ans = (ans + dp[k][i][j]) % p
            for j in [0, n + 1]:
                for i in range(1, m + 1):
                    ans = (ans + dp[k][i][j]) % p
        return ans


def main():
    # m = 2
    # n = 2
    # maxMove = 2
    # startRow = 0
    # startColumn = 0
    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1
    print(Solution().findPaths(m, n, maxMove, startRow, startColumn))


if __name__ == '__main__':
    main()

"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land,
find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells
(x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.



Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[10 ** 20 for j in range(n)] for i in range(n)]
        dp1 = [[10 ** 20 for j in range(n)] for i in range(n)]
        dp2 = [[10 ** 20 for j in range(n)] for i in range(n)]
        for i in range(n):
            j = 0
            while j < n and grid[i][j] != 1:
                j += 1
            cnt = 0
            while j < n:
                if grid[i][j] == 1:
                    cnt = 0
                    dp[i][j] = 0
                else:
                    cnt += 1
                    dp[i][j] = cnt
                j += 1

            j = n - 1
            while j >= 0 and grid[i][j] != 1:
                j -= 1
            cnt = 0
            while j >= 0:
                if grid[i][j] == 1:
                    cnt = 0
                else:
                    cnt += 1
                    dp[i][j] = min(dp[i][j], cnt)
                j -= 1

        for j in range(n):
            dp1[0][j] = dp[0][j]

        for i in range(1, n):
            for j in range(n):
                dp1[i][j] = min(dp[i][j], dp1[i - 1][j] + 1)

        for j in range(n):
            dp2[n - 1][j] = dp[n - 1][j]

        for i in reversed(range(n - 1)):
            for j in range(n):
                dp2[i][j] = min(dp[i][j], dp2[i + 1][j] + 1)

        best = 0
        for i in range(n):
            for j in range(n):
                best = max(best, min(dp1[i][j], dp2[i][j]))
        return best if 0 < best < 10 ** 20 else -1


def main():
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(Solution().maxDistance(grid))


if __name__ == '__main__':
    main()

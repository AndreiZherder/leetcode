"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally)
land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.



Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""
from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ans = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 1:
                    good = True
                    q = deque([(i, j)])
                    grid[i][j] = 0
                    cnt = 0
                    while q:
                        x, y = q.popleft()
                        cnt += 1
                        for dx, dy in steps:
                            nx, ny = x + dx, y + dy
                            if grid[nx][ny] == 1:
                                if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
                                    good = False
                                else:
                                    q.append((nx, ny))
                                grid[nx][ny] = 0
                    if good:
                        ans += cnt
        return ans


def main():
    grid = [[0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))


if __name__ == '__main__':
    main()

"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.



Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, length: int) -> int:
            ans = 0
            for di, dj in steps:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] != -1:
                        if (ni, nj) not in seen:
                            if grid[ni][nj] == 2:
                                if length + 1 == target:
                                    return 1
                                else:
                                    continue
                            seen.add((ni, nj))
                            ans += dfs(ni, nj, length + 1)
                            seen.remove((ni, nj))
            return ans

        steps = ((0, 1), (1, 0), (-1, 0), (0, -1))
        n = len(grid)
        m = len(grid[0])
        target = n * m
        x, y = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    target -= 1
                if grid[i][j] == 1:
                    x, y = i, j
        seen = {(x, y)}
        return dfs(x, y, 1)


def main():
    # grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    # grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    # grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
    grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
    # grid = [[0, 1], [2, 0]]
    print(Solution().uniquePathsIII(grid))


if __name__ == '__main__':
    main()

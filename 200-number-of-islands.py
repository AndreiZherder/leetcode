"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i: int, j: int):
            q = deque([(i, j)])
            while q:
                i, j = q.popleft()
                for di, dj in steps:
                    i1, j1 = i + di, j + dj
                    if (i1, j1) in cells:
                        q.append((i1, j1))
                        cells.remove((i1, j1))

        n = len(grid)
        m = len(grid[0])
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cells = {(i, j) for j in range(m) for i in range(n) if grid[i][j] == '1'}
        ans = 0
        while cells:
            ans += 1
            bfs(*cells.pop())
        return ans


def main():
    # grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))


if __name__ == '__main__':
    main()

"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell
(i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected
(i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import deque
from typing import List


class Solution:
    def is_inside_grid(self, i: int, j: int, n: int, m: int):
        return 0 <= i < n and 0 <= j < m

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[-1][-1] != 0:
            return -1
        neighbors = ((1, 1), (1, 0), (0, 1), (-1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1))
        cells = deque([(-1, -1, 0)])
        visited = set()
        while cells:
            i, j, level = cells.popleft()
            if (i, j) not in visited:
                visited.add((i, j))
                for di, dj in neighbors:
                    next_i = i + di
                    next_j = j + dj
                    if next_i == n - 1 and next_j == m - 1:
                        return level + 1
                    if self.is_inside_grid(next_i, next_j, n, m) and grid[next_i][next_j] == 0:
                        cells.append((next_i, next_j, level + 1))
        return -1


def main():
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(Solution().shortestPathBinaryMatrix(grid))


if __name__ == '__main__':
    main()

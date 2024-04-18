"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0
represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.



Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.

"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for di, dj in d4:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni == n:
                            ans += 1
                        if nj < 0 or nj == m:
                            ans += 1
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                            ans += 1
        return ans


def main():
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(Solution().islandPerimeter(grid))


if __name__ == '__main__':
    main()

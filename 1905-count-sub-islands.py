"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.



Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def inside(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n

        def check(points: List[List[int]]) -> int:
            for i, j in points:
                if grid1[i][j] == 0:
                    return 0
            return 1

        def dfs(i: int, j: int, points: List[List[int]]) -> List[List[int]]:
            if grid2[i][j] == 0:
                return []
            points.append([i, j])
            seen[i][j] = True
            for di, dj in steps:
                ni, nj = i + di, j + dj
                if inside(ni, nj) and not seen[ni][nj]:
                    dfs(ni, nj, points)

        m = len(grid1)
        n = len(grid1[0])
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = [[False for j in range(n)] for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if not seen[i][j]:
                    points = []
                    dfs(i, j, points)
                    if points:
                        ans += check(points)
        return ans


def main():
    grid1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    grid2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    print(Solution().countSubIslands(grid1, grid2))


if __name__ == '__main__':
    main()

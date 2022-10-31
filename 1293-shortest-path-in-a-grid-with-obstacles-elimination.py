"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def inside(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1:
            return 0
        visited = [[float('Inf') for j in range(m)] for i in range(n)]
        q = deque()
        q.append((0, 0, 0, 0))
        visited[0][0] = 0
        while q:
            i, j, eliminated, length = q.popleft()
            for di, dj in steps:
                ni = i + di
                nj = j + dj
                if ni == n - 1 and nj == m - 1:
                    return length + 1
                if inside(ni, nj):
                    if grid[ni][nj] == 1:
                        if eliminated < k:
                            if visited[ni][nj] > eliminated + 1:
                                visited[ni][nj] = eliminated + 1
                                q.append((ni, nj, eliminated + 1, length + 1))
                    else:
                        if visited[ni][nj] > eliminated:
                            visited[ni][nj] = eliminated
                            q.append((ni, nj, eliminated, length + 1))
        return -1


def main():
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    k = 1
    print(Solution().shortestPath(grid, k))


if __name__ == '__main__':
    main()

"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's.
There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
from collections import deque
from typing import List, Tuple


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def find_land(grid: List[List[int]]) -> Tuple[int, int]:
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j

        n = len(grid)
        i, j = find_land(grid)
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        island = deque([(i, j, 0)])
        grid[i][j] = 2
        q = deque([(i, j)])
        while q:
            i, j = q.popleft()
            for di, dj in steps:
                ni = i + di
                nj = j + dj
                if 0 <= ni and ni < n and 0 <= nj and nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj))
                    island.append((ni, nj, 0))
        while island:
            i, j, cnt = island.popleft()
            for di, dj in steps:
                ni = i + di
                nj = j + dj
                if 0 <= ni and ni < n and 0 <= nj and nj < n:
                    if grid[ni][nj] == 1:
                        return cnt
                    elif grid[ni][nj] == 0:
                        grid[ni][nj] = 2
                        island.append((ni, nj, cnt + 1))
        return -1


def main():
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    print(Solution().shortestBridge(grid))


if __name__ == '__main__':
    main()

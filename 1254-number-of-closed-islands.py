"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s
and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2


Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def find(i: int) -> int:
            while parent[i] != i:
                i = parent[i]
            return i

        def union(i: int, j: int):
            id1 = find(i)
            id2 = find(j)
            if id1 == id2:
                return
            if rank[id1] > rank[id2]:
                parent[id2] = id1
            else:
                parent[id1] = id2
                if rank[id1] == rank[id2]:
                    rank[id2] = rank[id1]

        n = len(grid)
        m = len(grid[0])
        parent = [i for i in range(m * n + 2)]
        rank = [0 for i in range(m * n + 2)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    if i == 0 or j == 0:
                        union(m * i + j, m * n)
                    else:
                        if grid[i - 1][j] == 0:
                            union(m * i + j, m * (i - 1) + j)
                        if grid[i][j - 1] == 0:
                            union(m * i + j, m * i + j - 1)
                        if i == n - 1 or j == m - 1:
                            union(m * i + j, m * n)
                else:
                    union(m * i + j, m * n + 1)
        return len({find(i) for i in range(m * n + 2)}) - 2


def main():
    grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    print(Solution().closedIsland(grid))


if __name__ == '__main__':
    main()

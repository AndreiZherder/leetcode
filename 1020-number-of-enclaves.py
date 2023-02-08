"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off
the boundary of the grid.

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
from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = DSU(n * m + 1)
        for j in range(m):
            if grid[0][j] == 1:
                dsu.union(j, m * n)
            if grid[n - 1][j] == 1:
                dsu.union((n - 1) * m + j, m * n)
        for i in range(n):
            if grid[i][0] == 1:
                dsu.union(i * m, m * n)
            if grid[i][m - 1] == 1:
                dsu.union((i + 1) * m - 1, m * n)
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1 and grid[i - 1][j] == 1:
                    dsu.union(i * m + j, (i - 1) * m + j)
                if grid[i][j] == 1 and grid[i][j - 1] == 1:
                    dsu.union(i * m + j, i * m + j - 1)
        outside_id = dsu.find(n * m)
        cnt = 0
        for i in range(n * m):
            if grid[i // m][i % m] != 0 and dsu.find(i) != outside_id:
                cnt += 1
        return cnt


def main():
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))


if __name__ == '__main__':
    main()

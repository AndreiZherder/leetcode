"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

"""
from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

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
            self.size[id1] += self.size[id2]
        else:
            self.parent[id1] = id2
            self.size[id2] += self.size[id1]
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def index(i: int, j: int):
            return i * m + j

        n = len(grid)
        m = len(grid[0])
        d4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
        dsu = DSU(n * m)
        for i in range(n):
            for j in range(m):
                for di, dj in d4:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if 1 == grid[i][j] == grid[ni][nj]:
                            dsu.union(index(i, j), index(ni, nj))
        ans = max(dsu.size)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    s = set()
                    for di, dj in d4:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            if grid[ni][nj] == 1:
                                s.add(dsu.find(index(ni, nj)))
                    ans = max(ans, 1 + sum(dsu.size[idx] for idx in s))
        return ans


def main():
    grid = [[1, 0], [0, 1]]
    print(Solution().largestIsland(grid))


if __name__ == '__main__':
    main()

"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '.
These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.



Example 1:
Input: grid = [" /","/ "]
Output: 2
Example 2:
Input: grid = [" /","  "]
Output: 1
Example 3:
Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.


Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.

"""
from collections import Counter
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
    def regionsBySlashes(self, grid: List[str]) -> int:
        def num(i: int, j: int, k: int) -> int:
            return i * n * 4 + j * 4 + k

        n = len(grid)
        dsu = DSU(n * n * 4)
        for j in range(1, n):
            dsu.union(num(0, j, 0), num(0, j - 1, 2))
        for i in range(1, n):
            dsu.union(num(i, 0, 1), num(i - 1, 0, 3))
        for i in range(1, n):
            for j in range(1, n):
                dsu.union(num(i, j, 0), num(i, j - 1, 2))
                dsu.union(num(i, j, 1), num(i - 1, j, 3))
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    dsu.union(num(i, j, 0), num(i, j, 1))
                    dsu.union(num(i, j, 2), num(i, j, 3))
                elif grid[i][j] == '\\':
                    dsu.union(num(i, j, 0), num(i, j, 3))
                    dsu.union(num(i, j, 1), num(i, j, 2))
                else:
                    dsu.union(num(i, j, 0), num(i, j, 1))
                    dsu.union(num(i, j, 1), num(i, j, 2))
                    dsu.union(num(i, j, 2), num(i, j, 3))
                    dsu.union(num(i, j, 3), num(i, j, 0))
        return len(Counter((dsu.find(x) for x in range(n * n * 4))))


def main():
    grid = [" /", "/ "]
    print(Solution().regionsBySlashes(grid))


if __name__ == '__main__':
    main()

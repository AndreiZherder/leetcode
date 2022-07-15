"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from itertools import chain
from typing import List


class Node:
    def __init__(self, parent: int):
        self.parent = parent
        self.rank = 0
        self.size = 1


class DSU:
    def __init__(self, n: int):
        self.nodes = [Node(i) for i in range(n)]
        self.max_size = 0

    def find(self, i: int) -> int:
        while i != self.nodes[i].parent:
            i = self.nodes[i].parent
        return i

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.nodes[id1].rank > self.nodes[id2].rank:
            self.nodes[id2].parent = id1
            self.nodes[id1].size += self.nodes[id2].size
            self.max_size = max(self.max_size, self.nodes[id1].size)
        else:
            self.nodes[id1].parent = id2
            self.nodes[id2].size += self.nodes[id1].size
            self.max_size = max(self.max_size, self.nodes[id2].size)
            if self.nodes[id1].rank == self.nodes[id2].rank:
                self.nodes[id2].rank += 1


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = DSU(n * m)
        for j in range(1, m):
            if grid[0][j] == 1 and grid[0][j - 1] == 1:
                dsu.union(j, j - 1)
        for i in range(1, n):
            if grid[i][0] == 1 and grid[i - 1][0] == 1:
                dsu.union(m * i, m * (i - 1))
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1 and grid[i][j - 1] == 1:
                    dsu.union(m * i + j, m * i + j - 1)
                if grid[i][j] == 1 and grid[i - 1][j] == 1:
                    dsu.union(m * i + j, m * (i - 1) + j)
        one = 0
        for num in chain.from_iterable(grid):
            if num == 1:
                one = 1
                break
        return dsu.max_size or one


def main():
    # grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    grid = [[0, 1]]
    print(Solution().maxAreaOfIsland(grid))


if __name__ == '__main__':
    main()

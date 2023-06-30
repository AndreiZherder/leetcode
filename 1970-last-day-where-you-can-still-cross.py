"""
There is a 1-based binary matrix where 0 represents land and 1 represents water.
You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water.
You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day,
the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells.
You can start from any cell in the top row and end at any cell in the bottom row.
You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.



Example 1:
Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:
Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:
Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.


Constraints:

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.

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
    def latestDayToCross(self, n: int, m: int, cells: List[List[int]]) -> int:
        def c(i: int, j: int) -> int:
            return i * m + j

        dsu = DSU((n + 2) * (m + 1))
        flooded = {tuple(cell) for cell in cells}
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for j in range(2, m + 1):
            dsu.union(c(0, j - 1), c(0, j))
        for i in range(1, n + 2):
            if (i, 1) not in flooded:
                if (i - 1, 1) not in flooded:
                    dsu.union(c(i, 1), c(i - 1, 1))
            for j in range(2, m + 1):
                if (i, j) not in flooded:
                    if (i, j - 1) not in flooded:
                        dsu.union(c(i, j), c(i, j - 1))
                    if (i - 1, j) not in flooded:
                        dsu.union(c(i, j), c(i - 1, j))
        ans = len(cells)
        for i, j in reversed(cells):
            if dsu.find(c(0, 1)) == dsu.find(c(n + 1, 1)):
                return ans
            for di, dj in steps:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n + 2 and 1 <= nj < m + 1:
                    if (ni, nj) not in flooded:
                        dsu.union(c(i, j), c(ni, nj))
            flooded.remove((i, j))
            ans -= 1
        return ans


def main():
    row = 3
    col = 3
    cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
    print(Solution().latestDayToCross(row, col, cells))


if __name__ == '__main__':
    main()

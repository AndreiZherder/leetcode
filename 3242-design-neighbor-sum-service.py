"""
You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].

Implement the neighborSum class:

neighborSum(int [][]grid) initializes the object.
int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the top,
left, right, or bottom of value in grid.
int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the
top-left, top-right, bottom-left, or bottom-right of value in grid.
Example 1:

Input:

["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]

[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]

Output: [null, 6, 16, 16, 4]

Explanation:
The adjacent neighbors of 1 are 0, 2, and 4.
The adjacent neighbors of 4 are 1, 3, 5, and 7.
The diagonal neighbors of 4 are 0, 2, 6, and 8.
The diagonal neighbor of 8 is 4.
Example 2:

Input:

["neighborSum", "adjacentSum", "diagonalSum"]

[[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]

Output: [null, 23, 45]

Explanation:
The adjacent neighbors of 15 are 0, 10, 7, and 6.
The diagonal neighbors of 9 are 4, 12, 14, and 15.


Constraints:

3 <= n == grid.length == grid[0].length <= 10
0 <= grid[i][j] <= n2 - 1
All grid[i][j] are distinct.
value in adjacentSum and diagonalSum will be in the range [0, n2 - 1].
At most 2 * n2 calls will be made to adjacentSum and diagonalSum.

"""
from typing import List


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        d4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dd4 = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        self.grid = grid
        self.d1 = dict()
        self.d2 = dict()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                total1 = 0
                total2 = 0
                for di, dj in d4:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        total1 += grid[ni][nj]
                for di, dj in dd4:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        total2 += grid[ni][nj]
                self.d1[grid[i][j]] = total1
                self.d2[grid[i][j]] = total2

    def adjacentSum(self, value: int) -> int:
        return self.d1[value]

    def diagonalSum(self, value: int) -> int:
        return self.d2[value]


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)


def main():
    ns = neighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(ns.adjacentSum(1))
    print(ns.adjacentSum(4))
    print(ns.diagonalSum(4))
    print(ns.diagonalSum(8))


if __name__ == '__main__':
    main()

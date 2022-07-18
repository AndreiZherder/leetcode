"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different:
for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8


Example 1:
"""
from collections import defaultdict
from typing import List


class AccumulatedSums2d:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.acc = [[0 for j in range(self.m + 1)] for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                self.acc[i][j] = self.acc[i - 1][j] +\
                                 self.acc[i][j - 1] -\
                                 self.acc[i - 1][j - 1] +\
                                 matrix[i - 1][j - 1]

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.acc[row2 + 1][col2 + 1] -\
               self.acc[row1][col2 + 1] -\
               self.acc[row2 + 1][col1] +\
               self.acc[row1][col1]


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        acc2d = AccumulatedSums2d(matrix)
        ans = 0
        for k in range(0, n):
            for i in range(0, n - k):
                d = defaultdict(int)
                d[0] = 1
                acc = 0
                for j in range(m):
                    acc += acc2d.sum_region(i, j, i + k, j)
                    ans += d.get(acc - target, 0)
                    d[acc] += 1
        return ans


def main():
    # matrix = [[1, -1], [-1, 1]]
    # target = 0
    matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))


if __name__ == '__main__':
    main()

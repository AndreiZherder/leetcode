"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0
(rows and columns are 0-indexed).



Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
"""
from itertools import product
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0 for i in range(n)]
        cols = [0 for j in range(m)]
        for i, j in product(range(n), range(m)):
            rows[i] += mat[i][j]
            cols[j] += mat[i][j]
        ans = 0
        for i in range(n):
            for j in range(m):
                if rows[i] == 1:
                    if cols[j] == 1:
                        if mat[i][j] == 1:
                            ans += 1
                else:
                    break
        return ans


def main():
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    print(Solution().numSpecial(mat))


if __name__ == '__main__':
    main()

"""
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target
by rotating mat in 90-degree increments, or false otherwise.



Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.


Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.

"""
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        f0 = True
        f90 = True
        f180 = True
        f270 = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    f0 = False
                if mat[i][j] != target[j][n - i - 1]:
                    f90 = False
                if mat[i][j] != target[n - i - 1][n - j - 1]:
                    f180 = False
                if mat[i][j] != target[n - j - 1][i]:
                    f270 = False
        return f0 or f90 or f180 or f270


def main():
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    print(Solution().findRotation(mat, target))


if __name__ == '__main__':
    main()

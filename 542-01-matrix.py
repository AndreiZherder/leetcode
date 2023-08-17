"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))
        n = len(mat)
        m = len(mat[0])
        ans = [[10 ** 20 for j in range(m)] for i in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j, 0))
        while q:
            i, j, d = q.popleft()
            for di, dj in d4:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if ans[ni][nj] > d + 1:
                        ans[ni][nj] = d + 1
                        q.append((ni, nj, d + 1))
        return ans


def main():
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().updateMatrix(mat))


if __name__ == '__main__':
    main()

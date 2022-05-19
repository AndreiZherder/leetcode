"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List


class Solution:
    def is_inside_grid(self, i: int, j: int, n: int, m: int):
        return 0 <= i < n and 0 <= j < m

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            max_depth = 1
            for di, dj in neighbors:
                if self.is_inside_grid(i + di, j + dj, n, m) and matrix[i + di][j + dj] > matrix[i][j]:
                    if (i + di, j + dj) in cache:
                        max_depth = max(max_depth, 1 + cache[(i + di, j + dj)])
                    else:
                        max_depth = max(max_depth, 1 + dfs(i + di, j + dj))
            cache[(i, j)] = max_depth
            return max_depth

        cache = {}
        n = len(matrix)
        m = len(matrix[0])
        neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for i in range(n):
            for j in range(m):
                if (i, j) not in cache:
                    dfs(i, j)
        return max(cache.values())


def main():
    matrix = [[1]]
    print(Solution().longestIncreasingPath(matrix))


if __name__ == '__main__':
    main()

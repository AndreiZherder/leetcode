"""
Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.

From the starting cell, you can move to any other cell in the same row or column,
but only if the value of the destination cell is strictly greater than the value of the current cell.
You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.

Return an integer denoting the maximum number of cells that can be visited.



Example 1:
Input: mat = [[3,1],[3,4]]
Output: 2
Explanation: The image shows how we can visit 2 cells starting from row 1, column 2.
It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2.
Example 2:
Input: mat = [[1,1],[1,1]]
Output: 1
Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example.
Example 3:
Input: mat = [[3,1,6],[-9,5,7]]
Output: 4
Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1.
It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4.


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 105
1 <= m * n <= 105
-105 <= mat[i][j] <= 105

"""
from typing import List

from sortedcontainers import SortedDict


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        def dp(i: int, j: int) -> int:
            if cache[i][j]:
                return cache[i][j]
            ans = 0
            x = rows[i].peekitem(rows[i].bisect_right(mat[i][j]))[1]
            y = cols[j].peekitem(cols[j].bisect_right(mat[i][j]))[1]
            ans = max(ans, x, y)
            ans += 1
            if not cache[i][j]:
                cache[i][j] = ans
            if mat[i][j] in rows[i]:
                rows[i][mat[i][j]] = max(rows[i][mat[i][j]], ans)
            else:
                rows[i][mat[i][j]] = ans
            if mat[i][j] in cols[j]:
                cols[j][mat[i][j]] = max(cols[j][mat[i][j]], ans)
            else:
                cols[j][mat[i][j]] = ans
            return ans

        n = len(mat)
        m = len(mat[0])
        rows = [SortedDict({100001: -10 ** 20}) for i in range(n)]
        cols = [SortedDict({100001: -10 ** 20}) for j in range(m)]
        cache = [[0 for j in range(m)] for i in range(n)]
        ans = 0
        for _, i, j in sorted(((mat[i][j], i, j) for i in range(n) for j in range(m)), reverse=True):
            if cache[i][j]:
                ans = max(ans, cache[i][j])
            else:
                ans = max(ans, dp(i, j))
        return ans


def main():
    mat = [[3, 1, 6], [-9, 5, 7]]
    print(Solution().maxIncreasingCells(mat))


if __name__ == '__main__':
    main()

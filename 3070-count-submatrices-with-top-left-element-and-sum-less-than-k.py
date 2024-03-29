"""
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of
submatrices
 that contain the top-left element of the grid, and have a sum less than or equal to k.



Example 1:
Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid,
and have a sum less than or equal to 18.
Example 2:
Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid,
and have a sum less than or equal to 20.


Constraints:

m == grid.length
n == grid[i].length
1 <= n, m <= 1000
0 <= grid[i][j] <= 1000
1 <= k <= 109

"""
from typing import List


def prefix_sum_2d(grid: List[List[int]]) -> List[List[int]]:
    """
    returns the 2d prefix sum array of size (n + 1) * (m + 1) with 0 on first row and first col
    """
    n = len(grid)
    m = len(grid[0])
    pref = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] + grid[i - 1][j - 1] - pref[i - 1][j - 1]
    return pref


def sum_2d(pref: List[List[int]], row1: int, col1: int, row2: int, col2: int) -> int:
    """
    returns sum of rectangle area [row1, col1] - (row2, col2)
    need to calculate prefix_sum_2d first
    """
    return pref[row2][col2] - pref[row1][col2] - pref[row2][col1] + pref[row1][col1]


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        pref = prefix_sum_2d(grid)
        ans = 0
        for i in range(n):
            for j in range(m):
                if sum_2d(pref, 0, 0, i + 1, j + 1) <= k:
                    ans += 1
                else:
                    break
        return ans


def main():
    grid = [[7, 2, 9], [1, 5, 0], [2, 6, 6]]
    k = 20
    print(Solution().countSubmatrices(grid, k))


if __name__ == '__main__':
    main()

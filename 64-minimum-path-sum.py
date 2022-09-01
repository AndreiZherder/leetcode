"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from itertools import accumulate
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = list(accumulate(grid[0]))
        dp1 = dp[:]
        for i in range(1, n):
            dp1[0] = dp[0] + grid[i][0]
            for j in range(1, m):
                dp1[j] = min(dp1[j - 1], dp[j]) + grid[i][j]
            dp, dp1 = dp1, dp
        return dp[-1]


def main():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))


if __name__ == '__main__':
    main()

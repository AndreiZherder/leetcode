"""
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.



Example 1:
Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation:
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:

Input: grid = [[7]]
Output: 7


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        dp = [grid[0][j] for j in range(n)]
        dp1 = [10 ** 20 for j in range(n)]
        for i in range(1, n):
            for j in range(n):
                for prevj in range(n):
                    if j != prevj:
                        dp1[j] = min(dp1[j], dp[prevj] + grid[i][j])
            dp, dp1 = dp1, [10 ** 20 for j in range(n)]
        return min(dp)


def main():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().minFallingPathSum(grid))


if __name__ == '__main__':
    main()

"""
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).



Example 1:
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1
"""
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        x = [-1 for i in range(n)]
        for i, row in enumerate(grid):
            cnt = 0
            for num in reversed(row):
                if num == 0:
                    cnt += 1
                else:
                    break
            x[i] = cnt

        ans = 0
        for i in range(n):
            if x[i] < n - i - 1:
                j = i + 1
                while j < n and x[j] < n - i - 1:
                    j += 1
                if j == n:
                    return -1
                else:
                    ans += j - i
                    for k in range(j, i, -1):
                        x[k], x[k - 1] = x[k - 1], x[k]
        return ans


def main():
    grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    print(Solution().minSwaps(grid))


if __name__ == '__main__':
    main()

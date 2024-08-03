"""
You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make all rows and columns palindromic,
and the total number of 1's in grid divisible by 4.



Example 1:

Input: grid = [[1,0,0],[0,1,0],[0,0,1]]

Output: 3

Explanation:
Example 2:

Input: grid = [[0,1],[0,1],[0,0]]

Output: 2

Explanation:
Example 3:

Input: grid = [[1],[1]]

Output: 2

Explanation:

Constraints:

m == grid.length
n == grid[i].length
1 <= m * n <= 2 * 105
0 <= grid[i][j] <= 1

"""
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def f(x: int) -> int:
            if x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return 2
            elif x % 4 == 3:
                return 1
            else:
                return 0

        n = len(grid)
        m = len(grid[0])
        top = 0
        bottom = n - 1
        ans = 0
        while top < bottom:
            left = 0
            right = m - 1
            while left < right:
                x = grid[top][left] + grid[top][right] + grid[bottom][left] + grid[bottom][right]
                ans += f(x)
                left += 1
                right -= 1
            top += 1
            bottom -= 1
        if n % 2 == 1:
            if m % 2 == 1:
                diff = 0
                ones = 0
                left = 0
                right = m - 1
                while left < right:
                    diff += grid[n // 2][left] ^ grid[n // 2][right]
                    ones += grid[n // 2][left] == 1 and grid[n // 2][right] == 1
                    left += 1
                    right -= 1
                top = 0
                bottom = n - 1
                while top < bottom:
                    diff += grid[top][m // 2] ^ grid[bottom][m // 2]
                    ones += grid[top][m // 2] == 1 and grid[bottom][m // 2] == 1
                    top += 1
                    bottom -= 1
                ones *= 2
                if diff > 0:
                    ans += diff
                else:
                    ans += ones % 4
                if grid[n // 2][m // 2] == 1:
                    ans += 1
            else:
                diff = 0
                ones = 0
                left = 0
                right = m - 1
                while left < right:
                    diff += grid[n // 2][left] ^ grid[n // 2][right]
                    ones += grid[n // 2][left] == 1 and grid[n // 2][right] == 1
                    left += 1
                    right -= 1
                ones *= 2
                if diff > 0:
                    ans += diff
                else:
                    ans += ones % 4
        else:
            if m % 2 == 1:
                diff = 0
                ones = 0
                top = 0
                bottom = n - 1
                while top < bottom:
                    diff += grid[top][m // 2] ^ grid[bottom][m // 2]
                    ones += grid[top][m // 2] == 1 and grid[bottom][m // 2] == 1
                    top += 1
                    bottom -= 1
                ones *= 2
                if diff > 0:
                    ans += diff
                else:
                    ans += ones % 4
        return ans


def main():
    grid = [[1, 0, 0, 1, 1, 1, 1]]
    print(Solution().minFlips(grid))


if __name__ == '__main__':
    main()

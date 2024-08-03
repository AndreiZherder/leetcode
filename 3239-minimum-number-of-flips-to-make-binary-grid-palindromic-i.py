"""
You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.



Example 1:

Input: grid = [[1,0,0],[0,0,0],[0,0,1]]

Output: 2

Explanation:
Flipping the highlighted cells makes all the rows palindromic.

Example 2:

Input: grid = [[0,1],[0,1],[0,0]]

Output: 1

Explanation:
Flipping the highlighted cell makes all the columns palindromic.

Example 3:

Input: grid = [[1],[0]]

Output: 0

Explanation:

All rows are already palindromic.



Constraints:

m == grid.length
n == grid[i].length
1 <= m * n <= 2 * 105
0 <= grid[i][j] <= 1

"""
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def solve(grid: List[List[int]]) -> int:
            n = len(grid)
            m = len(grid[0])
            ans = 0
            for i in range(n):
                j = 0
                k = m - 1
                while j < k:
                    ans += grid[i][j] ^ grid[i][k]
                    j += 1
                    k -= 1
            return ans

        a = solve(grid)
        b = solve([[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))])
        return min(a, b)


def main():
    grid = grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(Solution().minFlips(grid))


if __name__ == '__main__':
    main()

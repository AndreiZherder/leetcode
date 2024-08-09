"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.



Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
while this one is not:
In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15

"""
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(top: int, left: int) -> bool:
            row_sum = [0 for i in range(3)]
            col_sum = [0 for j in range(3)]
            seen = set()
            diag1_sum = 0
            diag2_sum = 0
            for i in range(3):
                for j in range(3):
                    row_sum[i] += grid[top + i][left + j]
                    col_sum[j] += grid[top + i][left + j]
                    seen.add(grid[top + i][left + j])
                diag1_sum += grid[top + i][left + i]
                diag2_sum += grid[top + 2 - i][left + i]
            return len(seen) == 9 and \
                all(num in seen for num in range(1, 10)) and \
                all(row_sum[i] == row_sum[0] for i in range(3)) and \
                all(col_sum[j] == row_sum[0] for j in range(3)) and \
                diag1_sum == row_sum[0] and \
                diag2_sum == row_sum[0]

        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n - 2):
            for j in range(m - 2):
                ans += check(i, j)
        return ans


def main():
    grid = [[3, 2, 9, 2, 7],
            [6, 1, 8, 4, 2],
            [7, 5, 3, 2, 7],
            [2, 9, 4, 9, 6],
            [4, 3, 8, 2, 5]]
    print(Solution().numMagicSquaresInside(grid))


if __name__ == '__main__':
    main()

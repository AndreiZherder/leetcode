"""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of
submatrices
 that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.


Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:
Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.



Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.

"""
from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        pref = [[0 for j in range(m + 1)] for i in range(n + 1)]
        ans = 0
        mini = n
        minj = m
        cur = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if grid[i - 1][j - 1] == 'X':
                    cur = -1
                    mini = min(mini, i - 1)
                    minj = min(minj, j - 1)
                elif grid[i - 1][j - 1] == 'Y':
                    cur = 1
                else:
                    cur = 0
                pref[i][j] = pref[i - 1][j] + pref[i][j - 1] + cur - pref[i - 1][j - 1]
                if pref[i][j] == 0 and mini <= i - 1 and minj <= j - 1:
                    ans += 1
        return ans


def main():
    grid = [["X", "Y", "."],
            ["Y", ".", "."]]
    print(Solution().numberOfSubmatrices(grid))


if __name__ == '__main__':
    main()

"""
You are given a 2D matrix grid of size m x n. In one operation, you can change the value of any cell to any non-negative number. You need to perform some operations such that each cell grid[i][j] is:

Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return the minimum number of operations needed.



Example 1:

Input: grid = [[1,0,2],[1,0,2]]

Output: 0

Explanation:
All the cells in the matrix already satisfy the properties.

Example 2:

Input: grid = [[1,1,1],[0,0,0]]

Output: 3

Explanation:
The matrix becomes [[1,0,1],[1,0,1]] which satisfies the properties, by doing these 3 operations:

Change grid[1][0] to 1.
Change grid[0][1] to 0.
Change grid[1][2] to 1.
Example 3:

Input: grid = [[1],[2],[3]]

Output: 2

Explanation:
here is a single column. We can change the value to 1 in each cell using 2 operations.



Constraints:

1 <= n, m <= 1000
0 <= grid[i][j] <= 9

"""
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(j: int, prev: int) -> int:
            if j == m:
                return 0
            ans = 10 ** 20
            for num in range(10):
                if num != prev:
                    ans = min(ans, n - cs[j][num] + dp(j + 1, num))
            return ans

        n = len(grid)
        m = len(grid[0])
        cs = [Counter() for j in range(m)]
        for i in range(n):
            for j in range(m):
                cs[j][grid[i][j]] += 1
        return dp(0, -1)


def main():
    grid = [[1, 1, 1], [0, 0, 0]]
    print(Solution().minimumOperations(grid))


if __name__ == '__main__':
    main()

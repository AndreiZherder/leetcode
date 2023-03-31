"""
Given a rectangular pizza represented as a rows x cols matrix containing the following characters:
'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

For each cut you choose the direction: vertical or horizontal,
then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically,
give the left part of the pizza to a person.
If you cut the pizza horizontally, give the upper part of the pizza to a person.
Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple.
Since the answer can be a huge number, return this modulo 10^9 + 7.



Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1


Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""
from functools import lru_cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
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

        @lru_cache(None)
        def dp(top: int, left: int, k: int) -> int:
            total = sum_2d(pref, top, left, n, m)
            if k == 1:
                return 1 if total > 0 else 0
            ans = 0
            for i in range(top, n - 1):
                if sum_2d(pref, top, left, i + 1, m):
                    ans = (ans + dp(i + 1, left, k - 1)) % mod
            for j in range(left, m - 1):
                if sum_2d(pref, top, left, n, j + 1):
                    ans = (ans + dp(top, j + 1, k - 1)) % mod
            return ans

        mod = 10 ** 9 + 7
        n = len(pizza)
        m = len(pizza[0])
        grid = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if pizza[i][j] == 'A':
                    grid[i][j] = 1
        pref = prefix_sum_2d(grid)

        return dp(0, 0, k)


def main():
    pizza = ["A..", "AAA", "..."]
    k = 3
    print(Solution().ways(pizza, k))


if __name__ == '__main__':
    main()

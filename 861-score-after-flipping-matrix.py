"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column
(i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).



Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.

"""
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] ^= 1
        for j in range(1, m):
            ones = 0
            zeroes = 0
            for i in range(n):
                if grid[i][j] == 1:
                    ones += 1
                else:
                    zeroes += 1
            if zeroes > ones:
                for i in range(n):
                    grid[i][j] ^= 1

        nums = [0 for i in range(n)]
        for i in range(n):
            for j in range(m):
                nums[i] |= grid[i][m - j - 1] << j
        return sum(nums)


def main():
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(Solution().matrixScore(grid))


if __name__ == '__main__':
    main()

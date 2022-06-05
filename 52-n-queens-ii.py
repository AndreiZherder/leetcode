"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.



Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""
from typing import List, Tuple


class Solution:
    def __init__(self):
        self.ans = 0

    def two_queens_attack(self, i1: int, j1: int, i2: int, j2: int):
        return i1 == i2 or j1 == j2 or abs(i1 - i2) == abs(j1 - j2)

    def put_queen(self, n: int, queens: List[Tuple[int, int]], i: int, j: int):
        if any(self.two_queens_attack(i1, j1, i, j) for i1, j1 in queens):
            return
        if j == n - 1:
            self.ans += 1
        else:
            queens.append((i, j))
            for k in range(n):
                self.put_queen(n, queens, k, j + 1)
            queens.pop()

    def totalNQueens(self, n: int) -> int:
        for k in range(n):
            self.put_queen(n, [], k, 0)
        return self.ans


def main():
    n = 8
    print(Solution().totalNQueens(n))


if __name__ == '__main__':
    main()

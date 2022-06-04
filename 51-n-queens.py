"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space, respectively.



Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
from typing import List, Tuple


class Solution:
    def make_board(self, n: int, queens: List[Tuple[int, int]]) -> List[str]:
        board = [['.' for j in range(n)] for i in range(n)]
        for i, j in queens:
            board[i][j] = 'Q'
        return [''.join(board[i]) for i in range(n)]

    def two_queens_attack(self, i1: int, j1: int, i2: int, j2: int):
        return i1 == i2 or j1 == j2 or abs(i1 - i2) == abs(j1 - j2)

    def put_queen(self, n: int, queens: List[Tuple[int, int]], i: int, j: int, ans: List[List[str]]):
        if any(self.two_queens_attack(i1, j1, i, j) for i1, j1 in queens):
            return
        if j == n - 1:
            ans.append(self.make_board(n, queens + [(i, j)]))
        else:
            queens.append((i, j))
            for k in range(n):
                self.put_queen(n, queens, k, j + 1, ans)
            queens.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        for k in range(n):
            self.put_queen(n, [], k, 0, ans)
        return ans


def main():
    n = 9
    for board in Solution().solveNQueens(n):
        for row in board:
            print(row)
        print()


if __name__ == '__main__':
    main()

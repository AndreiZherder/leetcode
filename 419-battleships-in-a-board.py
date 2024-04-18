"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board.
In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
where k can be of any size. At least one horizontal or vertical cell separates between two battleships
(i.e., there are no adjacent battleships).



Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.


Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        ans = 0
        if board[0][0] == 'X':
            ans += 1
        for j in range(1, m):
            if board[0][j] == 'X' and board[0][j - 1] != 'X':
                ans += 1
        for i in range(1, n):
            if board[i][0] == 'X' and board[i - 1][0] != 'X':
                ans += 1
            for j in range(1, m):
                if board[i][j] == 'X' and board[i][j - 1] != 'X' and board[i - 1][j] != 'X':
                    ans += 1
        return ans


def main():
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    print(Solution().countBattleships(board))


if __name__ == '__main__':
    main()

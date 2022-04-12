"""
According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state:
live (represented by a 1) or dead (represented by a 0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # if the sum of all nine fields in a given neighbourhood is three,
        # the inner field state for the next generation will be life;
        # if the all-field sum is four, the inner field retains its current state;
        # and every other sum sets the inner field to death
        n = len(board)
        m = len(board[0])
        prev_row = []
        for i in range(n):
            cur_row = board[i].copy()
            next_row = board[i + 1] if i + 1 < n else []
            for j in range(m):
                neigh_sum = self.neighbors_sum(j, cur_row, prev_row, next_row)
                if neigh_sum == 3:
                    board[i][j] = 1
                elif neigh_sum == 4:
                    continue
                else:
                    board[i][j] = 0
            prev_row = cur_row

    def neighbors_sum(self, j: int, cur_row: List[int], prev_row: List[int], next_row: List[int]) -> int:
        ans = 0
        m = len(cur_row)
        if prev_row:
            if j == 0 and j == m - 1:
                ans += prev_row[j]
            elif j == 0:
                ans += prev_row[j] + prev_row[j + 1]
            elif j == m - 1:
                ans += prev_row[j - 1] + prev_row[j]
            else:
                ans += prev_row[j - 1] + prev_row[j] + prev_row[j + 1]
        if j == 0 and j == m - 1:
            ans += cur_row[j]
        elif j == 0:
            ans += cur_row[j] + cur_row[j + 1]
        elif j == m - 1:
            ans += cur_row[j - 1] + cur_row[j]
        else:
            ans += cur_row[j - 1] + cur_row[j] + cur_row[j + 1]
        if next_row:
            if j == 0 and j == m - 1:
                ans += next_row[j]
            elif j == 0:
                ans += next_row[j] + next_row[j + 1]
            elif j == m - 1:
                ans += next_row[j - 1] + next_row[j]
            else:
                ans += next_row[j - 1] + next_row[j] + next_row[j + 1]
        return ans


def main():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    print(board)


if __name__ == '__main__':
    main()

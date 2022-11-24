"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int):
            id1 = find(i)
            id2 = find(j)
            if id1 == id2:
                return
            if rank[id1] > rank[id2]:
                parent[id2] = id1
            else:
                parent[id1] = id2
                if rank[id1] == rank[id2]:
                    rank[id2] += 1

        n = len(board)
        m = len(board[0])
        parent = [i for i in range(n * m + 1)]
        rank = [0 for i in range(n * m + 1)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                        union(i * m + j, n * m)
                    if i > 0 and board[i - 1][j] == 'O':
                        union(i * m + j, (i - 1) * m + j)
                    if j > 0 and board[i][j - 1] == 'O':
                        union(i * m + j, i * m + j - 1)

        border_id = find(n * m)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and find(i * m + j) != border_id:
                    board[i][j] = 'X'


def main():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print(Solution().solve(board))
    print(board)


if __name__ == '__main__':
    main()

"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0.
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved.
If it is impossible for the state of the board to be solved, return -1.



Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]


Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.

"""
from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def next_states(v: str) -> List[str]:
            d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))
            ans = []
            x = v.find('0')
            j = x % 3
            i = x // 3
            for di, dj in d4:
                ni, nj = i + di, j + dj
                if 0 <= ni < 2 and 0 <= nj < 3:
                    u = list(v)
                    u[ni * 3 + nj], u[i * 3 + j] = u[i * 3 + j], u[ni * 3 + nj]
                    u = ''.join(u)
                    ans.append(u)
            return ans

        start = ''.join(map(str, board[0] + board[1]))
        target = '123450'
        if start == target:
            return 0
        q = deque()
        seen = set()
        q.append((start, 0))
        seen.add(start)
        while q:
            v, step = q.popleft()
            for u in next_states(v):
                if u == target:
                    return step + 1
                if u not in seen:
                    seen.add(u)
                    q.append((u, step + 1))
        return -1


def main():
    board = [[4, 1, 2], [5, 0, 3]]
    print(Solution().slidingPuzzle(board))


if __name__ == '__main__':
    main()

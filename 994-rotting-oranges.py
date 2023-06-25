"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q, q1 = deque(), deque()
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    cnt += 1
        if cnt == 0:
            return 0
        elif not q:
            return -1
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ans = 0
        while q:
            ans += 1
            while q:
                i, j = q.popleft()
                for di, dj in steps:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        cnt -= 1
                        grid[ni][nj] = 2
                        q1.append((ni, nj))
            q, q1 = q1, q
        return ans - 1 if cnt == 0 else -1


def main():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(Solution().orangesRotting(grid))


if __name__ == '__main__':
    main()

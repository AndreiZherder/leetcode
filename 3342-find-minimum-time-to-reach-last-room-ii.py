"""
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j]
represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0)
at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move
and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.



Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 4



Constraints:

2 <= n == moveTime.length <= 750
2 <= m == moveTime[i].length <= 750
0 <= moveTime[i][j] <= 109

"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        d4 = ((1, 0),(0, -1), (-1, 0), (0, 1))
        seen = [[False for j in range(m)] for i in range(n)]
        seen[0][0] = True
        q = [(0, 0, 0)]
        while q:
            cur, i, j = heappop(q)
            for di, dj in d4:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and not seen[ni][nj]:
                    if ni == n - 1 and nj == m - 1:
                        return max(moveTime[ni][nj] + (i + j) % 2 + 1, cur + (i + j) % 2 + 1)
                    seen[ni][nj] = True
                    heappush(q, (max(moveTime[ni][nj] + (i + j) % 2 + 1, cur + (i + j) % 2 + 1), ni, nj))
        return -1


def main():
    moveTime = [[0, 4], [4, 4]]
    print(Solution().minTimeToReach(moveTime))


if __name__ == '__main__':
    main()

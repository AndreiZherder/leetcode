"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer
arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent
the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting
from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one
guard that can see it.

Return the number of unoccupied cells that are not guarded.



Example 1:
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.


Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.

"""
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def go(di: int, dj: int):
            seen = set()
            for i, j in guards:
                i += di
                j += dj
                while 0 <= i < n and 0 <= j < m and (i, j) not in walls and (i, j) not in seen:
                    grid[i][j] = 0
                    seen.add((i, j))
                    i += di
                    j += dj

        n, m = m, n
        d4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
        guards = {(i, j) for i, j in guards}
        walls = {(i, j) for i, j in walls}
        grid = [[1 for j in range(m)] for i in range(n)]
        for i, j in guards:
            grid[i][j] = 0
        for i, j in walls:
            grid[i][j] = 0
        for di, dj in d4:
            go(di, dj)
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += grid[i][j]
        return ans


def main():
    m = 4
    n = 6
    guards = [[0, 0], [1, 1], [2, 3]]
    walls = [[0, 1], [2, 2], [1, 4]]
    print(Solution().countUnguarded(m, n, guards, walls))


if __name__ == '__main__':
    main()

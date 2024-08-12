"""
You are given an m x n binary grid grid where 1 represents land and 0 represents water.
An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.



Example 1:
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:
Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.

"""
from collections import defaultdict
from typing import List

d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def connected() -> bool:
            def dfs(v) -> int:
                ans = 1
                for u in g[v]:
                    if u not in seen:
                        seen.add(u)
                        ans += dfs(u)
                return ans

            if not land:
                return False
            n = len(land)
            start = land.pop()
            seen = {start}
            ans = dfs(start) == n
            land.add(start)
            return ans

        n = len(grid)
        m = len(grid[0])
        land = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land.add((i, j))
        g = defaultdict(set)
        for v in land:
            i, j = v
            for di, dj in d4:
                ni = i + di
                nj = j + dj
                if (ni, nj) in land:
                    g[v].add((ni, nj))
        if not connected():
            return 0
        for v in land:
            saved_childs = g[v].copy()
            land.remove(v)
            for u in g[v]:
                g[u].remove(v)
            g[v].clear()
            if not connected():
                return 1
            land.add(v)
            g[v] = saved_childs
            for u in saved_childs:
                g[u].add(v)
        return 2


def main():
    grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().minDays(grid))


if __name__ == '__main__':
    main()

"""
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix
and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in,
then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4
directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed
to visit the same cell multiple times.

Return the resulting array answer.



Example 1:
Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:
Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106

"""
from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        k = len(queries)
        order = sorted(range(k), key=lambda i: queries[i])
        d4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = [0 for i in range(k)]
        q = deque()
        q1 = []
        cur = 0
        heappush(q1, (grid[0][0], 0, 0))
        seen = set()
        for i in order:
            limit = queries[i]
            while q1 and q1[0][0] < limit:
                val, x, y = heappop(q1)
                q.append((x, y))
                seen.add((x, y))
                cur += 1
            while q:
                x, y = q.popleft()
                for dx, dy in d4:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] < limit:
                            if (nx, ny) not in seen:
                                q.append((nx, ny))
                                seen.add((nx, ny))
                                cur += 1
                        else:
                            if (nx, ny) not in seen:
                                heappush(q1, (grid[nx][ny], nx, ny))
                                seen.add((nx, ny))
            ans[i] = cur
        return ans


def main():
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5, 6, 2]
    print(Solution().maxPoints(grid, queries))


if __name__ == '__main__':
    main()

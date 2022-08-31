"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east,
and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci]
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
"""
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def inside(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def bfs_pacific():
            q = deque()
            for j in range(m):
                q.append((0, j))
                pacific.add((0, j))
            for i in range(1, n):
                q.append((i, 0))
                pacific.add((i, 0))
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    i1, j1 = i + di, j + dj
                    if (i1, j1) not in pacific and inside(i1, j1) and heights[i1][j1] >= heights[i][j]:
                        pacific.add((i1, j1))
                        q.append((i1, j1))

        def bfs_atlantic() -> List[List[int]]:
            ans = []
            q = deque()
            for j in range(m):
                q.append((n - 1, j))
                atlantic.add((n - 1, j))
                if (n - 1, j) in pacific:
                    ans.append([n - 1, j])
            for i in range(n - 1):
                q.append((i, m - 1))
                atlantic.add((i, m - 1))
                if (i, m - 1) in pacific:
                    ans.append([i, m - 1])
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    i1, j1 = i + di, j + dj
                    if (i1, j1) not in atlantic and inside(i1, j1) and heights[i1][j1] >= heights[i][j]:
                        atlantic.add((i1, j1))
                        q.append((i1, j1))
                        if (i1, j1) in pacific:
                            ans.append([i1, j1])
            return ans

        pacific = set()
        atlantic = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        n = len(heights)
        m = len(heights[0])
        bfs_pacific()
        return bfs_atlantic()


def main():
    # heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    # heights = [[1]]
    heights = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(Solution().pacificAtlantic(heights))


if __name__ == '__main__':
    main()

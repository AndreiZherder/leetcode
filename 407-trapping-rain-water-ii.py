"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map,
return the volume of water it can trap after raining.



Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10


Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104

"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        ans = 0
        d4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = []
        seen = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            heappush(q, (heightMap[i][0], i, 0))
            seen[i][0] = True
            if not seen[i][m - 1]:
                heappush(q, (heightMap[i][m - 1], i, m - 1))
                seen[i][m - 1] = True
        for j in range(m):
            if not seen[0][j]:
                heappush(q, (heightMap[0][j], 0, j))
                seen[0][j] = True
            if not seen[n - 1][j]:
                heappush(q, (heightMap[n - 1][j], n - 1, j))
                seen[n - 1][j] = True
        while q:
            h, i, j = heappop(q)
            for di, dj in d4:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and not seen[ni][nj]:
                    seen[ni][nj] = True
                    if heightMap[ni][nj] < h:
                        ans += h - heightMap[ni][nj]
                    heappush(q, (max(h, heightMap[ni][nj]), ni, nj))
        return ans


def main():
    heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    print(Solution().trapRainWater(heightMap))


if __name__ == '__main__':
    main()

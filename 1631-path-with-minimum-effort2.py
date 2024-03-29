"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0),
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells,
which is better than route [1,3,5,3,5].
Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^6
"""
from collections import deque
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def bsl(left: int, right: int) -> int:
            """
            FFFFTTTT
                |
            """
            def check(mid: int) -> bool:
                q = deque([(0, 0)])
                seen = {(0, 0)}
                while q:
                    i, j = q.popleft()
                    for di, dj in d4:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in seen and abs(heights[ni][nj] - heights[i][j]) <= mid:
                            if ni == n - 1 and nj == m - 1:
                                return True
                            seen.add((ni, nj))
                            q.append((ni, nj))
                return False

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))
        n = len(heights)
        m = len(heights[0])
        if n == m == 1:
            return 0
        return bsl(0, 10 ** 6)



def main():
    heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
    print(Solution().minimumEffortPath(heights))


if __name__ == '__main__':
    main()

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
        n = len(heights)
        m = len(heights[0])
        if n == 1 and m == 1:
            return 0
        left = 0
        right = 1000000
        while left <= right:
            k = (left + right) // 2
            if self.bfs(heights, 0, 0, k, set()):
                right = k - 1
            else:
                left = k + 1
        return left

    def bfs(self, heights: List[List[int]], i: int, j: int, k: int, visited: set) -> bool:
        n = len(heights)
        m = len(heights[0])
        nodes = deque([(i, j)])
        visited.add((i, j))
        while nodes:
            i, j = nodes.popleft()
            if i + 1 < n and (i + 1, j) not in visited and abs(heights[i][j] - heights[i + 1][j]) <= k:
                if i + 1 == n - 1 and j == m - 1:
                    return True
                nodes.append((i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < m and (i, j + 1) not in visited and abs(heights[i][j] - heights[i][j + 1]) <= k:
                if i == n - 1 and j + 1 == m - 1:
                    return True
                nodes.append((i, j + 1))
                visited.add((i, j + 1))
            if i - 1 >= 0 and (i - 1, j) not in visited and abs(heights[i][j] - heights[i - 1][j]) <= k:
                if i - 1 == n - 1 and j == m - 1:
                    return True
                nodes.append((i - 1, j))
                visited.add((i - 1, j))
            if j - 1 >= 0 and (i, j - 1) not in visited and abs(heights[i][j] - heights[i][j - 1]) <= k:
                if i == n - 1 and j - 1 == m - 1:
                    return True
                nodes.append((i, j - 1))
                visited.add((i, j - 1))
        return False


def main():
    heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
    print(Solution().minimumEffortPath(heights))


if __name__ == '__main__':
    main()

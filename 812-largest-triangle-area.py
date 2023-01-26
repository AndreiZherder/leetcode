"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi],
return the area of the largest triangle that can be formed by any three different points.
Answers within 10-5 of the actual answer will be accepted.



Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000


Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
"""
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        best = 0
        for i in range(n - 2):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    s = abs((y2 - y3) * (x1 - x3) - (x2 - x3) * (y1 - y3)) / 2
                    best = max(best, s)
        return best


def main():
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(Solution().largestTriangleArea(points))


if __name__ == '__main__':
    main()

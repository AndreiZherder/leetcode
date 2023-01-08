"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.



Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        points.sort()
        d = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2:
                    d[(1000000, x1)] |= {(x1, y1), (x2, y2)}
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                    d[(k, b)] |= {(x1, y1), (x2, y2)}
        return max(len(s) for s in d.values())


def main():
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(Solution().maxPoints(points))


if __name__ == '__main__':
    main()

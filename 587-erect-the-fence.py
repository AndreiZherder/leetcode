"""
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive.
The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
Example 2:
Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]


Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
"""
from typing import List, Tuple


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def cmp_by_angle(point: List[int]) -> Tuple[float, int]:
            x, y = point
            if x == x0:
                return float('Inf'), -y
            angle = (y - y0) / (x - x0)
            return angle, x

        def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
            return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) >= 0

        n = len(points)
        if n < 3:
            return points

        x0, y0 = min(points)

        if all(x == points[0][0] for x, y in points):
            return points
        x1, y1 = points[1]
        if x1 - x0 != 0:
            angle = (y1 - y0) / (x1 - x0)
            flag = True
            for i in range(2, n):
                x2, y2 = points[i]
                if x2 - x0 == 0:
                    flag = False
                    break
                if (y2 - y0) / (x2 - x0) != angle:
                    flag = False
                    break
            if flag:
                return points

        points.sort(key=cmp_by_angle)
        stack = [[x0, y0], points[0]]
        for i in range(1, n):
            x1, y1 = stack[-2]
            x2, y2 = stack[-1]
            x3, y3 = points[i]
            while len(stack) >= 2 and not ccw(x1, y1, x2, y2, x3, y3):
                stack.pop()
                x1, y1 = stack[-2]
                x2, y2 = stack[-1]
            stack.append(points[i])
        stack.pop()

        x1, y1 = stack[-1]
        if x1 - x0 != 0:
            angle = (y1 - y0) / (x1 - x0)
            i = n - 3
            x2, y2 = points[i]
            cur_angle = (y2 - y0) / (x2 - x0)
            while cur_angle == angle:
                stack.append(points[i])
                i -= 1
                x2, y2 = points[i]
                cur_angle = (y2 - y0) / (x2 - x0)
        return stack


def main():
    points = [[0, 0], [0, 100], [100, 100], [100, 0]]
    print(Solution().outerTrees(points))


if __name__ == '__main__':
    main()

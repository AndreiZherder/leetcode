"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if all(x == x1 for x, y in coordinates):
            return True
        if x2 - x1 == 0:
            return False
        k = (y2 - y1) / (x2 - x1)
        for i in range(1, n):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]
            if k * (x2 - x1) != y2 - y1:
                return False
        return True


def main():
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(Solution().checkStraightLine(coordinates))


if __name__ == '__main__':
    main()

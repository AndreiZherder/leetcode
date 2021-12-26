"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:

1 <= k <= points.length <= 104
-10^4 < xi, yi < 10^4
"""
import random
from functools import total_ordering
from typing import List


@total_ordering
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2

    def __eq__(self, other):
        return self.x ** 2 + self.y ** 2 == other.x ** 2 + other.y ** 2


def partition(a: List[Point], l: int, r: int):
    rand = random.randrange(l, r + 1)
    a[l], a[rand] = a[rand], a[l]
    x = a[l]
    j1 = l
    j2 = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
    for i in range(l + 1, j2 + 1):
        if a[i] < x:
            j1 += 1
            a[i], a[j1] = a[j1], a[i]
    a[l], a[j1] = a[j1], a[l]
    a[j1], a[j2] = a[j2], a[j1]
    return j1, j2


def random_select(points: List[Point], l: int, r: int, k) -> List[Point]:
    if l >= r:
        return [points[l]]
    m1, m2 = partition(points, l, r)
    if l <= k < m1:
        return random_select(points, l, m1 - 1, k)
    elif m1 <= k <= m2:
        return points[l:k + 1]
    else:
        return points[l:m2 + 1] + random_select(points, m2 + 1, r, k)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = 0
        r = len(points) - 1
        kpoints = random_select([Point(point[0], point[1]) for point in points], l, r, k - 1)
        return [[point.x, point.y] for point in kpoints]


def main():
    print(Solution().kClosest([[3, 3], [4, 4], [2, 2], [2, 2], [2, 2], [1, 1]], 5))


if __name__ == '__main__':
    main()

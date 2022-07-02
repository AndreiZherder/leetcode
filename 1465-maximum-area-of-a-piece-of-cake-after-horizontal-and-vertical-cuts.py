"""
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays
horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 10^9 + 7.



Example 1:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
After you cut the cake, the green piece of cake has the maximum area.
Example 2:
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9


Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length <= min(h - 1, 10^5)
1 <= verticalCuts.length <= min(w - 1, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
All the elements in horizontalCuts are distinct.
All the elements in verticalCuts are distinct.
"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        height = max((horizontalCuts[i + 1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1)), default=0)
        height = max(height, horizontalCuts[0])
        height = max(height, h - horizontalCuts[-1])

        width = max((verticalCuts[i + 1] - verticalCuts[i] for i in range(len(verticalCuts) - 1)), default=0)
        width = max(width, verticalCuts[0])
        width = max(width, w - verticalCuts[-1])

        return (height * width) % (10 ** 9 + 7)


def main():
    # h = 5
    # w = 4
    # horizontalCuts = [1, 2, 4]
    # verticalCuts = [1, 3]
    # h = 5
    # w = 4
    # horizontalCuts = [3, 1]
    # verticalCuts = [1]
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))


if __name__ == '__main__':
    main()

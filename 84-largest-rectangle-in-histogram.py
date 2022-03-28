"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        limits = [[0, 0] for i in range(len(heights))]
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                limits[stack.pop()][1] = i - 1
            stack.append(i)
        while stack and heights[stack[-1]] > 0:
            limits[stack.pop()][1] = len(heights) - 1

        for i, height in enumerate(reversed(heights)):
            while stack and heights[stack[-1]] > height:
                limits[stack.pop()][0] = len(heights) - i
            stack.append(len(heights) - i - 1)
        while stack and heights[stack[-1]] > 0:
            limits[stack.pop()][0] = 0

        maximum = 0
        for limit, height in zip(limits, heights):
            maximum = max(maximum, (limit[1] - limit[0] + 1) * height)
        return maximum


def main():
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))


if __name__ == '__main__':
    main()

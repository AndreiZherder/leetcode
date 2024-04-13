"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1


Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
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

        n = len(matrix)
        m = len(matrix[0])
        best = 0
        heights = [[0 for i in range(m)] for i in range(n)]
        for j in range(m):
            heights[0][j] = int(matrix[0][j])
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if heights[i - 1][j] != 0:
                        heights[i][j] = heights[i - 1][j] + 1
                    else:
                        heights[i][j] = 1
        for i in range(n):
            best = max(best, largestRectangleArea(heights[i]))
        return best


def main():
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(matrix))


if __name__ == '__main__':
    main()

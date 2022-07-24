"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisect_left_row(matrix: List[List[int]], row: int, left: int, right: int, target: int):
            while left <= right:
                mid = left + (right - left) // 2
                if target <= matrix[row][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def bisect_left_col(matrix: List[List[int]], col: int, top: int, bottom: int, target: int):
            while top <= bottom:
                mid = top + (bottom - top) // 2
                if target <= matrix[mid][col]:
                    bottom = mid - 1
                else:
                    top = mid + 1
            return top

        def bisect_right_row(matrix: List[List[int]], row: int, left: int, right: int, target: int):
            while left <= right:
                mid = left + (right - left) // 2
                if target < matrix[row][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def bisect_right_col(matrix: List[List[int]], col: int, top: int, bottom: int, target: int):
            while top <= bottom:
                mid = top + (bottom - top) // 2
                if target < matrix[mid][col]:
                    bottom = mid - 1
                else:
                    top = mid + 1
            return top

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        while left < right or top < bottom:
            prev_right = right
            prev_left = left
            prev_top = top
            prev_bottom = bottom
            right = bisect_right_row(matrix, top, left, right, target) - 1
            bottom = bisect_right_col(matrix, left, top, bottom, target) - 1
            left = bisect_left_row(matrix, bottom, left, right, target)
            if left > len(matrix[0]) - 1:
                return False
            top = bisect_left_col(matrix, right, top, bottom, target)
            if top > len(matrix) - 1:
                return False
            if target < matrix[top][left] or target > matrix[bottom][right]:
                return False
            if prev_left == left and prev_right == right and prev_top == top and prev_bottom == bottom:
                return True
        if matrix[top][left] == target:
            return True
        else:
            return False


def main():
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(Solution().searchMatrix(matrix, matrix[i][j]))
    print(Solution().searchMatrix(matrix, 0))
    print(Solution().searchMatrix(matrix, 40))
    print(Solution().searchMatrix(matrix, 29))
    # matrix = [[-1, 3]]
    # target = 3
    # matrix = [[1, 1]]
    # target = 1
    # print(Solution().searchMatrix(matrix, target))


if __name__ == '__main__':
    main()

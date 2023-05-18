"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top = 1
        bottom = n
        left = 0
        right = m
        total = m * n
        i = 0
        j = 0
        k = 0
        ans = []
        while k < total:
            while k < total and j < right:
                ans.append(matrix[i][j])
                k += 1
                j += 1
            j -= 1
            i += 1
            right -= 1
            while k < total and i < bottom:
                ans.append(matrix[i][j])
                k += 1
                i += 1
            i -= 1
            j -= 1
            bottom -= 1
            while k < total and j >= left:
                ans.append(matrix[i][j])
                k += 1
                j -= 1
            j += 1
            i -= 1
            left += 1
            while k < total and i >= top:
                ans.append(matrix[i][j])
                k += 1
                i -= 1
            i += 1
            j += 1
            top += 1
        return ans


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))


if __name__ == '__main__':
    main()

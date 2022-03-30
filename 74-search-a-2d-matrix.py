"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List


class Solution:
    def value(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix[0])
        i = k // m
        j = k - i * m
        return matrix[i][j]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            val = self.value(matrix, m)
            if val == target:
                return True
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        return False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 2
    print(Solution().searchMatrix(matrix, target))


if __name__ == '__main__':
    main()

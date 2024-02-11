"""
Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer.
ake answer equal to matrix,
then replace each element with the value -1 with the maximum element in its respective column.

Return the matrix answer.



Example 1:
Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Output: [[1,2,9],[4,8,6],[7,8,9]]
Explanation: The diagram above shows the elements that are changed (in blue).
- We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
- We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.
Example 2:
Input: matrix = [[3,-1],[5,2]]
Output: [[3,2],[5,2]]
Explanation: The diagram above shows the elements that are changed (in blue).


Constraints:

m == matrix.length
n == matrix[i].length
2 <= m, n <= 50
-1 <= matrix[i][j] <= 100
The input is generated such that each column contains at least one non-negative integer.

"""
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        mx = [-1 for j in range(m)]
        for i in range(n):
            for j in range(m):
                mx[j] = max(mx[j], matrix[i][j])
        ans = [[matrix[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if ans[i][j] == -1:
                    ans[i][j] = mx[j]
        return ans


def main():
    matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
    print(Solution().modifiedMatrix(matrix))


if __name__ == '__main__':
    main()

"""
iven an m x n matrix matrix and an integer k,
return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.



Example 1:
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10^5 <= k <= 10^5


Follow up: What if the number of rows is much larger than the number of columns?
"""
from typing import List

from sortedcontainers import SortedSet


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.acc = [[0 for j in range(self.m + 1)] for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                self.acc[i][j] = self.acc[i - 1][j] + \
                                 self.acc[i][j - 1] - \
                                 self.acc[i - 1][j - 1] + \
                                 matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.acc[row2 + 1][col2 + 1] - \
               self.acc[row1][col2 + 1] - \
               self.acc[row2 + 1][col1] + \
               self.acc[row1][col1]


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(nums: List[int], k) -> int:
            s = SortedSet()
            ans = -float('Inf')
            s.add(0)
            for num in nums:
                i = s.bisect_left(num - k)
                if i < len(s):
                    ans = max(ans, num - s[i])
                s.add(num)
            return ans

        n = len(matrix)
        m = len(matrix[0])
        if n > m:
            matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]
            n, m = m, n

        ans = -float('Inf')
        acc = NumMatrix(matrix)
        for h in range(n):
            for i in range(n - h):
                nums = [acc.sumRegion(i, 0, i + h, j) for j in range(m)]
                ans = max(ans, maxSumSubarray(nums, k))
        return ans


def main():
    # matrix = [[1, 0, 1], [0, -2, 3]]
    # k = 2
    matrix = [[2, 2, -1]]
    k = 3
    print(Solution().maxSumSubmatrix(matrix, k))


if __name__ == '__main__':
    main()

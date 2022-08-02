"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2


Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity?
The solution may be too advanced for an interview but you may find reading this paper fun.
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        num = matrix[0][0]
        h = [(num, 0, 0)]
        seen = {(0, 0)}
        for step in range(k):
            num, i, j = heappop(h)
            if i + 1 < n:
                if (i + 1, j) not in seen:
                    heappush(h, (matrix[i + 1][j], i + 1, j))
                    seen.add((i + 1, j))
                else:
                    seen.remove((i + 1, j))
            if j + 1 < n:
                if (i, j + 1) not in seen:
                    heappush(h, (matrix[i][j + 1], i, j + 1))
                    seen.add((i, j + 1))
                else:
                    seen.remove((i, j + 1))
        return num


def main():
    # matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    # k = 8
    matrix = [[1, 3, 6], [5, 8, 10], [7, 9, 11]]
    k = 9
    print(Solution().kthSmallest(matrix, k))


if __name__ == '__main__':
    main()

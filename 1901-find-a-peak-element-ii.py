"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left,
right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j]
and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.



Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.

"""
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def divide_and_conquer(left: int, right: int) -> List[int]:
            if left == right:
                mx = mat[0][left]
                ans = [0, left]
                for i in range(n):
                    if mat[i][left] > mx:
                        mx = mat[i][left]
                        ans = [i, left]
                return ans
            else:
                mid = left + (right - left) // 2
                mx = mat[0][mid]
                ans = [0, mid]
                for i in range(n):
                    if mat[i][mid] > mx:
                        mx = mat[i][mid]
                        ans = [i, mid]
                    if mid - 1 >= left:
                        if mat[i][mid - 1] > mx:
                            mx = mat[i][mid - 1]
                            ans = [i, mid - 1]
                    if mid + 1 <= right:
                        if mat[i][mid + 1] > mx:
                            mx = mat[i][mid + 1]
                            ans = [i, mid + 1]
                if ans[1] == mid:
                    return ans
                elif ans[1] == mid - 1:
                    return divide_and_conquer(left, mid - 1)
                else:
                    return divide_and_conquer(mid + 1, right)

        n = len(mat)
        m = len(mat[0])
        return divide_and_conquer(0, m - 1)


def main():
    mat = [[20, 43, 38, 24, 31],
           [36, 34, 23, 28, 48],
           [22, 23, 45, 30, 18],
           [20, 17, 15, 8, 47],
           [13, 21, 8, 48, 35],
           [49, 45, 12, 13, 14],
           [48, 31, 18, 47, 38],
           [49, 34, 39, 19, 7]]
    print(Solution().findPeakGrid(mat))


if __name__ == '__main__':
    main()

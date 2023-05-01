"""
You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.



Example 1:
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order,
and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].


Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.
"""
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rpainted = [0 for i in range(n)]
        cpainted = [0 for i in range(m)]
        d = dict()
        for i in range(n):
            for j in range(m):
                d[mat[i][j]] = (i, j)
        for k, num in enumerate(arr):
            i, j = d[num]
            rpainted[i] += 1
            cpainted[j] += 1
            if rpainted[i] == m or cpainted[j] == n:
                return k
        return -1


def main():
    arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
    mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
    print(Solution().firstCompleteIndex(arr, mat))


if __name__ == '__main__':
    main()

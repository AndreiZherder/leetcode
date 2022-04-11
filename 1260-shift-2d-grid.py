"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""
import itertools
from typing import List


class Solution:
    def reverse(self, a: List, i: int, j: int):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    def rotate(self, a: List, k: int):
        n = len(a)
        self.reverse(a, 0, n - k - 1)
        self.reverse(a, n - k, n - 1)
        self.reverse(a, 0, n - 1)

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        a = list(itertools.chain(*grid))
        self.rotate(a, k % (n * m))
        return [[a[j] for j in range(i * m, (i + 1) * m)] for i in range(n)]


def main():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(Solution().shiftGrid(grid, k))


if __name__ == '__main__':
    main()

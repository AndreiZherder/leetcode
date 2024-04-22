"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east.
The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid.
Whenever you move outside the grid's boundary, we continue our walk outside the grid
(but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.



Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],
[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols

"""
from itertools import cycle
from typing import List


class Solution:
    def spiralMatrixIII(self, n: int, m: int, rStart: int, cStart: int) -> List[List[int]]:
        d4 = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
        ans = [[rStart, cStart]]
        step = 1
        cur = 1
        i = rStart
        j = cStart
        while cur < n * m:
            for _ in range(2):
                step += 1
                diff = step // 2
                di, dj = next(d4)
                row_target = i + di * diff
                col_target = j + dj * diff
                while i != row_target or j != col_target:
                    i += di
                    j += dj
                    if 0 <= i < n and 0 <= j < m:
                        cur += 1
                        ans.append([i, j])
        return ans




def main():
    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    print(Solution().spiralMatrixIII(rows, cols, rStart, cStart))


if __name__ == '__main__':
    main()

"""
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0
if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], n = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
Example 2:

Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
Output: [0,0,1,1,1,1,1,0]


Constraints:

cells.length == 8
cells[i] is either 0 or 1.
1 <= n <= 10^9
"""
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        x = 0
        for num in cells:
            x = (x << 2) + num
        seen = {x: 0}
        d = {0: cells[:]}
        dp = [0 for i in range(8)]
        for i in range(1, min(256, n + 1)):
            for j in range(1, 7):
                dp[j] = cells[j - 1] ^ cells[j + 1] ^ 1
            x = 0
            for num in dp:
                x = (x << 2) + num
            if x in seen:
                start = seen[x]
                cycle_len = i - start
                break
            else:
                seen[x] = i
                d[i] = dp[:]
            cells[0] = 0
            cells[7] = 0
            cells, dp = dp, cells
        else:
            return cells
        return d[start + (n - start) % cycle_len]


def main():
    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    n = 1000000000
    print(Solution().prisonAfterNDays(cells, n))


if __name__ == '__main__':
    main()

"""
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices
given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1
going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign,
only the relevant area of the plus sign is checked for 1's.



Example 1:
Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:
Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.


Constraints:

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
All the pairs (xi, yi) are unique.
"""
from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        for row, col in mines:
            rows[row].append(col)
            cols[col].append(row)
        for row in rows:
            rows[row].sort()
        for col in cols:
            cols[col].sort()

        ans = 0
        for i in range(n):
            for j in range(n):

                if i in rows:
                    index = bisect_right(rows[i], j) - 1
                    if index == -1:
                        left_len = j + 1
                    else:
                        left_len = j - rows[i][index]
                else:
                    left_len = j + 1

                if i in rows:
                    index += 1
                    if index == len(rows[i]):
                        right_len = n - j
                    else:
                        right_len = rows[i][index] - j
                else:
                    right_len = n - j

                if j in cols:
                    index = bisect_right(cols[j], i) - 1
                    if index == -1:
                        top_len = i + 1
                    else:
                        top_len = i - cols[j][index]
                else:
                    top_len = i + 1

                if j in cols:
                    index += 1
                    if index == len(cols[j]):
                        bottom_len = n - i
                    else:
                        bottom_len = cols[j][index] - i
                else:
                    bottom_len = n - i

                ans = max(ans, min(left_len, right_len, top_len, bottom_len))

        return ans


def main():
    n = 5
    mines = [[1, 0], [1, 4], [2, 4], [3, 2], [4, 0], [4, 3]]
    print(Solution().orderOfLargestPlusSign(n, mines))


if __name__ == '__main__':
    main()

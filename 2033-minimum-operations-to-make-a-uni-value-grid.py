"""
You are given a 2D integer grid of size m x n and an integer x.
In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.



Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following:
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= x, grid[i][j] <= 10^4
"""
from itertools import chain
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        i = 0
        j = n * m - 1
        nums = list(chain.from_iterable(grid))
        nums.sort()
        i = 0
        j = n * m - 1
        ans = 0
        while i < j:
            if (nums[j] - nums[i]) % x == 0:
                ans += (nums[j] - nums[i]) // x
                i += 1
                j -= 1
            else:
                return -1
        if n * m % 2 == 1 and n * m >= 3:
            if (nums[i] - nums[i - 1]) % x != 0 or (nums[j + 1] - nums[j]) % x != 0:
                return -1
        return ans


def main():
    grid = [[2, 4], [6, 8]]
    x = 2
    print(Solution().minOperations(grid, x))


if __name__ == '__main__':
    main()

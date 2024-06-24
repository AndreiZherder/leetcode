"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area,
such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.



Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:
The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[0,0],[1,0]]

Output: 1

Explanation:
The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.



Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.

"""
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mini = 10 ** 20
        maxi = 0
        minj = 10 ** 20
        maxj = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mini = min(mini, i)
                    maxi = max(maxi, i)
                    minj = min(minj, j)
                    maxj = max(maxj, j)
        return (maxi - mini + 1) * (maxj - minj + 1)


def main():
    grid = [[0, 1, 0], [1, 0, 1]]
    print(Solution().minimumArea(grid))


if __name__ == '__main__':
    main()

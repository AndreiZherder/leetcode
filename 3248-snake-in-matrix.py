"""
There is a snake in an n x n matrix grid and can move in four possible directions.
Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.

The snake starts at cell 0 and follows a sequence of commands.

You are given an integer n representing the size of the grid and an array of strings commands where each command[i]
is either "UP", "RIGHT", "DOWN", and "LEFT". It's guaranteed that the snake will remain within the grid boundaries
throughout its movement.

Return the position of the final cell where the snake ends up after executing commands.



Example 1:

Input: n = 2, commands = ["RIGHT","DOWN"]

Output: 3

Explanation:
Example 2:

Input: n = 3, commands = ["DOWN","RIGHT","UP"]

Output: 1

Explanation:
Constraints:

2 <= n <= 10
1 <= commands.length <= 100
commands consists only of "UP", "RIGHT", "DOWN", and "LEFT".
The input is generated such the snake will not move outside of the boundaries.

"""
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = 0
        j = 0
        for cmd in commands:
            if cmd == 'UP':
                i -= 1
            elif cmd == 'DOWN':
                i += 1
            elif cmd == 'LEFT':
                j -= 1
            else:
                j += 1
        return i * n + j


def main():
    n = 2
    commands = ["RIGHT","DOWN"]
    print(Solution().finalPositionOfSnake(n, commands))


if __name__ == '__main__':
    main()

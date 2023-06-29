"""
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions.
You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English
alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key;
and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.



Example 1:
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:
Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:
Input: grid = ["@Aa"]
Output: -1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.

"""
from collections import defaultdict, deque
from typing import List


def mask(c: str) -> int:
    return 1 << (ord(c.lower()) - ord('a'))


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        target = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start = (i, j)
                if grid[i][j] in 'abcdef':
                    target |= mask(grid[i][j])
        target |= 1 << 6
        i, j = start
        q = deque()
        q.append((i, j, 1 << 6, 0))
        seen = defaultdict(set)
        seen[(i, j)].add(1 << 6)
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while q:
            i, j, keys, cnt = q.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#':
                    if keys in seen[(ni, nj)]:
                        continue
                    else:
                        nkeys = keys
                        if grid[ni][nj] in 'ABCDEF' and not mask(grid[ni][nj]) & keys:
                            continue
                        if grid[ni][nj] in 'abcdef':
                            nkeys |= mask(grid[ni][nj])
                            if nkeys == target:
                                return cnt + 1
                        seen[(ni, nj)].add(nkeys)
                        q.append((ni, nj, nkeys, cnt + 1))
        return -1


def main():
    grid = [".#.b.", "A.#aB", "#d...", "@.cC.", "D...#"]
    print(Solution().shortestPathAllKeys(grid))


if __name__ == '__main__':
    main()

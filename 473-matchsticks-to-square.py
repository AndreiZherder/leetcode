"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.



Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
"""
from functools import lru_cache
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i: int, acc: int, k: int, visited: int) -> bool:
            if k == 0:
                return True
            if acc == length:
                return dfs(0, 0, k - 1, visited)
            if i == n:
                return False
            if visited & (1 << i) == 0 and matchsticks[i] + acc <= length:
                visited |= (1 << i)
                if dfs(i + 1, matchsticks[i] + acc, k, visited):
                    return True
                visited &= ~(1 << i)
            return dfs(i + 1, acc, k, visited)

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4
        n = len(matchsticks)
        visited = 0
        return dfs(0, 0, 4, visited)


def main():
    # matchsticks = [1, 1, 2, 2, 2]
    # matchsticks = [5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]
    # matchsticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]
    matchsticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(Solution().makesquare(matchsticks))


if __name__ == '__main__':
    main()

"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from functools import lru_cache
from typing import List


class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        @lru_cache(None)
        def dfs(i: int, total: int) -> List[List[int]]:
            ans = []
            if total + c[i] == target:
                return [[c[i]]]
            if total + c[i] < target:
                for j in range(i + 1, n):
                    if j == i + 1 or c[j] != c[j - 1]:
                        for seq in dfs(j, total + c[i]):
                            ans.append([c[i]] + seq)
            return ans

        c.sort()
        ans = []
        n = len(c)
        for i in range(n):
            if i == 0 or c[i] != c[i - 1]:
                for seq in dfs(i, 0):
                    ans.append(seq)
        return ans

def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))


if __name__ == '__main__':
    main()

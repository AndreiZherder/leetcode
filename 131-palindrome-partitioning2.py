"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""
from functools import lru_cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache(None)
        def dfs(i: int) -> List[List[str]]:
            ans = []
            for j in range(i + 1, n + 1):
                if s[i:j] == s[i:j][::-1]:
                    if j == n:
                        ans.append([s[i:j]])
                    else:
                        for path in dfs(j):
                            ans.append([s[i:j]] + path)
            return ans

        n = len(s)
        return dfs(0)


def main():
    s = "aabab"
    print(Solution().partition(s))


if __name__ == '__main__':
    main()

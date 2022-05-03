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
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        a = [['' for j in range(n)] for i in range(n)]
        for i in range(n):
            for k in range(2):
                left = i
                right = i + k
                while left >= 0 and right < n:
                    if s[left] == s[right]:
                        a[left][right] = s[left:right + 1]
                    else:
                        break
                    left -= 1
                    right += 1
        return self.dfs(a, 0)

    def dfs(self, a: List[List[str]], j: int):
        n = len(a)
        i = j
        ans = []
        for j in range(i, n):
            if a[i][j]:
                lsts = self.dfs(a, j + 1)
                if lsts:
                    for lst in lsts:
                        ans.append([a[i][j]] + lst)
                else:
                    ans.append([a[i][j]])
        return ans


def main():
    s = "aabab"
    print(Solution().partition(s))


if __name__ == '__main__':
    main()

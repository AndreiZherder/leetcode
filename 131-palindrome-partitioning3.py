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
        def backtrack(i: int, cur: List[str]):
            if i == n:
                ans.append(cur.copy())
            for j in range(i, n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    cur.append(s[i:j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()

        n = len(s)
        ans = []
        backtrack(0, [])
        return ans


def main():
    s = "aabab"
    print(Solution().partition(s))


if __name__ == '__main__':
    main()

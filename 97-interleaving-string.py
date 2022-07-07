"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache()
        def helper(i: int, j: int, k: int) -> bool:
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False
            if s1[i] == s3[k] and s2[j] == s3[k]:
                return any((helper(i + 1, j, k + 1),
                            helper(i, j + 1, k + 1)))
            if s1[i] == s3[k]:
                return helper(i + 1, j, k + 1)
            else:
                return helper(i, j + 1, k + 1)

        if len(s1) + len(s2) != len(s3):
            return False
        return helper(0, 0, 0)


def main():
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbbaccc"
    # s1 = "aabd"
    # s2 = "abdc"
    # s3 = "aabdbadc"
    s1 = "aaaa"
    s2 = "aa"
    s3 = "aaa"
    print(Solution().isInterleave(s1, s2, s3))


if __name__ == '__main__':
    main()

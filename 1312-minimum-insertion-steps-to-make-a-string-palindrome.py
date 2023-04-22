"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.



Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        def longestPalindromeSubseq(s: str) -> int:
            @lru_cache(None)
            def dp(i: int, j: int) -> int:
                if i > j:
                    return 0
                if i == j:
                    return 1
                if s[i] == s[j]:
                    return 2 + dp(i + 1, j - 1)
                else:
                    return max(dp(i, j - 1), dp(i + 1, j))

            return dp(0, len(s) - 1)
        return len(s) - longestPalindromeSubseq(s)


def main():
    s = "leetcode"
    print(Solution().minInsertions(s))


if __name__ == '__main__':
    main()

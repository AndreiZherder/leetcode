"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.



Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.


Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.

"""
from functools import lru_cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i == -1 and j == -1:
                return 0
            if i == -1:
                return dp(-1, j - 1) + ord(s2[j])
            if j == -1:
                return dp(i - 1, -1) + ord(s1[i])
            if s1[i] == s2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i - 1, j) + ord(s1[i]), dp(i, j - 1) + ord(s2[j]))
        return dp(len(s1) - 1, len(s2) - 1)


def main():
    s1 = "delete"
    s2 = "leet"
    print(Solution().minimumDeleteSum(s1, s2))


if __name__ == '__main__':
    main()

"""
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single
character by a different character such that the resulting substring is a substring of t. In other words,
find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a',
so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.
Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
The underlined portions are the substrings that are chosen from s and t.


Constraints:

1 <= s.length, t.length <= 100
s and t consist of lowercase English letters only.

"""
from collections import Counter
from string import ascii_lowercase
from typing import List


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        target = Counter()
        n = len(t)
        for i in range(n):
            for j in range(i + 1, n + 1):
                target[t[i:j]] += 1
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                for k in range(i, j):
                    for c in ascii_lowercase:
                        s1 = ''.join((s[i:k], c, s[k + 1:j]))
                        if c != s[k] and s1 in target:
                            ans += target[s1]
        return ans


def main():
    s = "aba"
    t = "baba"
    print(Solution().countSubstrings(s, t))


if __name__ == '__main__':
    main()

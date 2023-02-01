"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
from itertools import zip_longest
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        k = gcd(len(str1), len(str2))
        g1 = (str1[i:i + k] for i in range(0, len(str1), k))
        g2 = (str2[i:i + k] for i in range(0, len(str2), k))
        for a, b in zip_longest(g1, g2, fillvalue=str1[:k]):
            if a != b:
                return ''
        return str1[:k]


def main():
    str1 = "ABABAB"
    str2 = "ABAB"
    print(Solution().gcdOfStrings(str1, str2))


if __name__ == '__main__':
    main()

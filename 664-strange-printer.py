"""
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and
will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.



Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string,
which will cover the existing character 'a'.


Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
"""
from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i == j:
                return 1
            if i > j:
                return 0
            best = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    best = min(best, dp(i, k - 1) + dp(k + 1, j))
            return best
        return dp(0, len(s) - 1)


def main():
    s = "aba"
    print(Solution().strangePrinter(s))


if __name__ == '__main__':
    main()

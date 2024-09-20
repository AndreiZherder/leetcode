"""
You are given a string s. You can convert s to a
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.



Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.

"""
from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def prefix_function(s: str):
            a = s + "#" + s[::-1]
            n = len(a)
            pref = [0] * n
            c = 0
            for i in range(1, n):
                while c != 0 and a[c] != a[i]:
                    c = pref[c - 1]
                if a[c] == a[i]:
                    c += 1
                pref[i] = c
            return c

        c = prefix_function(s)
        return s[c:][::-1] + s


def main():
    s = "aacecaaa"
    print(Solution().shortestPalindrome(s))


if __name__ == '__main__':
    main()

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s: str, i: int, j: int, cnt: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    if cnt == 1:
                        return False
                    if helper(s, i + 1, j, cnt + 1):
                        return True
                    else:
                        return helper(s, i, j - 1, cnt + 1)
                else:
                    i += 1
                    j -= 1
            return True
        return helper(s, 0, len(s) - 1, 0)


def main():
    s = "abc"
    print(Solution().validPalindrome(s))


if __name__ == '__main__':
    main()

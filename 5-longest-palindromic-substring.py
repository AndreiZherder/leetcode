"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        length = 0
        ans = ''
        for i in range(n):
            for k in range(2):
                left = i
                right = i + k
                while left >= 0 and right < n:
                    if s[left] == s[right]:
                        if right - left + 1 > length:
                            length = right - left + 1
                            ans = s[left:right + 1]
                    else:
                        break
                    left -= 1
                    right += 1
        return ans


def main():
    s = "bababdddd"
    print(Solution().longestPalindrome(s))


if __name__ == '__main__':
    main()

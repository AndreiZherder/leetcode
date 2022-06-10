"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        j = 0
        ans = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                ans = max(ans, i - j)
                prev_j = j
                j = d[c] + 1
                for c1 in s[prev_j:j]:
                    del d[c1]
                d[c] = i
        ans = max(ans, len(s) - j)
        return ans


def main():
    s = "beaconwwkeswatqoil"
    print(Solution().lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()

"""
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
"""
from collections import Counter


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0
        ans = 0
        cur = Counter(s[:3])
        ans = int(len(cur) == 3)
        for i in range(3, n):
            cur[s[i - 3]] -= 1
            if cur[s[i - 3]] == 0:
                del cur[s[i - 3]]
            cur[s[i]] += 1
            ans += len(cur) == 3
        return ans


def main():
    s = "aababcabc"
    print(Solution().countGoodSubstrings(s))


if __name__ == '__main__':
    main()

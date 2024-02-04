"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        n = len(s)
        j = 0
        cur = Counter()
        best = 10 ** 20
        ans = ''
        for i in range(n):
            cur[s[i]] += 1
            while all(cur[c] >= target[c] for c in target):
                if i - j + 1 < best:
                    best = i - j + 1
                    ans = s[j:i + 1]
                cur[s[j]] -= 1
                j += 1
        return ans


def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))


if __name__ == '__main__':
    main()

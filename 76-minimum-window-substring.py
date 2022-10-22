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
        def check(k: int) -> bool:
            window = Counter(s[:k])
            if all(window[c] >= pattern[c] for c in pattern):
                return True
            for i in range(1, n - k + 1):
                window[s[i - 1]] -= 1
                if window[s[i - 1]] == 0:
                    del window[s[i - 1]]
                window[s[i + k - 1]] += 1
                if all(window[c] >= pattern[c] for c in pattern):
                    return True
            return False

        n = len(s)
        pattern = Counter(t)

        left = len(t)
        right = n
        if left > right:
            left = n + 1
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        if left == n + 1:
            return ""
        else:
            window = Counter(s[:left])
            if all(window[c] >= pattern[c] for c in pattern):
                return s[:left]
            for i in range(1, n - left + 1):
                window[s[i - 1]] -= 1
                if window[s[i - 1]] == 0:
                    del window[s[i - 1]]
                window[s[i + left - 1]] += 1
                if all(window[c] >= pattern[c] for c in pattern):
                    return s[i:i + left]


def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))


if __name__ == '__main__':
    main()

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n])
        if cnt1 == cnt2:
            return True
        for i in range(n, m):
            cnt2[s2[i - n]] -= 1
            if cnt2[s2[i - n]] == 0:
                del cnt2[s2[i - n]]
            cnt2[s2[i]] += 1
            if cnt1 == cnt2:
                return True
        return False


def main():
    print(Solution().checkInclusion('rvwrk', 'lznomzggwrvrkxecjaq'))


if __name__ == '__main__':
    main()

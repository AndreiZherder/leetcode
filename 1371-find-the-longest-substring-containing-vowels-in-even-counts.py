"""
Given the string s, return the size of the longest substring containing each vowel an even number of times.
That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels:
e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels:
a, e, i, o and u appear zero times.


Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.

"""
from typing import List


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        pref = [0]
        for c in s:
            if c in vowels:
                pref.append(pref[-1] ^ vowels[c])
            else:
                pref.append(pref[-1])
        d = dict()
        ans = 0
        for i, num in enumerate(pref):
            if num not in d:
                d[num] = i
            else:
                ans = max(ans, i - d[num])
        return ans


def main():
    s = "eleetminicoworoep"
    print(Solution().findTheLongestSubstring(s))


if __name__ == '__main__':
    main()

"""
Given a string s, return the maximum length of a
substring
 such that it contains at most two occurrences of each character.


Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.

"""
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = Counter()
        n = len(s)
        j = 0
        best = 0
        for i in range(n):
            counter[s[i]] += 1
            while any(counter[c] > 2 for c in counter):
                counter[s[j]] -= 1
                j += 1
            best = max(best, i - j + 1)
        return best



def main():
    s = "bcbbbcba"
    print(Solution().maximumLengthSubstring(s))


if __name__ == '__main__':
    main()

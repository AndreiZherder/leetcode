"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c
are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c
are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

"""
from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        j = 0
        counter = Counter()
        for i in range(n):
            counter[s[i]] += 1
            while len(counter) == 3:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    del counter[s[j]]
                j += 1
            ans += i - j + 1
        return n * (n + 1) // 2 - ans


def main():
    s = "abcabc"
    print(Solution().numberOfSubstrings(s))


if __name__ == '__main__':
    main()

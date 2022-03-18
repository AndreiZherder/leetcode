"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        d = Counter(s)
        seen = set()
        for c in s:
            if c in seen:
                d[c] -= 1
            else:
                while ans and ans[-1] >= c and d[ans[-1]] > 1:
                    d[ans[-1]] -= 1
                    seen.discard(ans[-1])
                    ans.pop()
                ans.append(c)
                seen.add(c)
        return ''.join(ans)


def main():
    # s = 'cbacdcbc'
    s = "abacb"
    print(Solution().removeDuplicateLetters(s))


if __name__ == '__main__':
    main()

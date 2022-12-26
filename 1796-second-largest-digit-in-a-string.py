"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.



Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.


Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
from heapq import heappush, heappushpop


class Solution:
    def secondHighest(self, s: str) -> int:
        h = []
        seen = set()
        for c in s:
            if c.isdigit():
                if c not in seen:
                    seen.add(c)
                    if len(h) < 2:
                        heappush(h, int(c))
                    else:
                        heappushpop(h, int(c))
        if len(h) < 2:
            return -1
        return h[0]




def main():
    s = "dfa12321afd"
    print(Solution().secondHighest(s))


if __name__ == '__main__':
    main()

"""
Given a string s and an integer k, return the length of the longest substring of s such
that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105

"""
from collections import Counter
from typing import List


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def divide_and_conquer(s: str) -> int:
            if len(s) < k:
                return 0
            n = len(s)
            counter = Counter(s)
            bad = {c for c, v in counter.items() if v < k}
            if not bad:
                return n
            a = [False if s[i] in bad else True for i in range(n)]
            arr = []
            ans = 0
            for i in range(n):
                if a[i]:
                    arr.append(s[i])
                else:
                    ans = max(ans, divide_and_conquer(''.join(arr)))
                    arr = []
            ans = max(ans, divide_and_conquer(''.join(arr)))
            return ans

        return divide_and_conquer(s)


def main():
    s = 'aaabb'
    k = 3
    print(Solution().longestSubstring(s, k))


if __name__ == '__main__':
    main()

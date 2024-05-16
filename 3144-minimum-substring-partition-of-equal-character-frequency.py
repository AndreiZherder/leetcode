"""
Given a string s, you need to partition it into one or more balanced
substrings
. For example, if s == "ababcc" then ("abab", "c", "c"), ("ab", "abc", "c"), and ("ababcc") are all valid partitions,
but ("a", "bab", "cc"), ("aba", "bc", "c"), and ("ab", "abcc") are not. The unbalanced substrings are bolded.

Return the minimum number of substrings that you can partition s into.

Note: A balanced string is a string where each character in the string occurs the same number of times.



Example 1:

Input: s = "fabccddg"

Output: 3

Explanation:

We can partition the string s into 3 substrings in one of the following ways: ("fab, "ccdd", "g"),
or ("fabc", "cd", "dg").

Example 2:

Input: s = "abababaccddb"

Output: 2

Explanation:

We can partition the string s into 2 substrings like so: ("abab", "abaccddb").



Constraints:

1 <= s.length <= 1000
s consists only of English lowercase letters.

"""
from collections import Counter
from functools import lru_cache


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            if i == n:
                return 0
            ans = 10 ** 20
            c = Counter()
            for j in range(i, n):
                c[s[j]] += 1
                x = c[s[j]]
                if all(v == x for v in c.values()):
                    ans = min(ans, 1 + dp(j + 1))
            return ans
        n = len(s)
        return dp(0)


def main():
    s = "abababaccddb"
    print(Solution().minimumSubstringsInPartition(s))


if __name__ == '__main__':
    main()

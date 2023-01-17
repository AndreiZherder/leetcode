"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none),
followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.



Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.


Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""
from functools import lru_cache


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def dfs(i: int, zeroes: int) -> int:
            if zeroes == n - i:
                return 0
            j = i
            while s[j] == '0':
                j += 1
            zeroes -= j - i
            i = j
            while i < n and s[i] == '1':
                i += 1
            return min(i - j + dfs(i, zeroes), zeroes)

        n = len(s)
        return dfs(0, s.count('0'))


def main():
    s = "00110"
    print(Solution().minFlipsMonoIncr(s))


if __name__ == '__main__':
    main()

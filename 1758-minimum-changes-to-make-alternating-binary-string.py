"""
You are given a string s consisting only of the characters '0' and '1'.
In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.



Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".


Constraints:

1 <= s.length <= 10^4
s[i] is either '0' or '1'.
"""
from itertools import cycle


class Solution:
    def minOperations(self, s: str) -> int:
        ans1 = 0
        ans2 = 0
        g1 = cycle(['0', '1'])
        g2 = cycle(['1', '0'])
        for c, a, b in zip(s, g1, g2):
            if c != a:
                ans1 += 1
            if c != b:
                ans2 += 1
        return min(ans1, ans2)


def main():
    s = "0100"
    print(Solution().minOperations(s))


if __name__ == '__main__':
    main()
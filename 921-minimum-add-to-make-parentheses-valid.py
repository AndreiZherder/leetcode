"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.



Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3


Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.

"""
from typing import List


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif cnt != 0:
                cnt -= 1
            else:
                ans += 1
        return ans + cnt


def main():
    s = "())"
    print(Solution().minAddToMakeValid(s))


if __name__ == '__main__':
    main()

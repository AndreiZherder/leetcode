"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


Constraints:

1 <= s.length <= 10^5
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for_delete = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    for_delete.append(i)
        for_delete += stack
        ans = []
        prev = 0
        for i in for_delete:
            ans.append(s[prev:i])
            prev = i + 1
        ans.append(s[prev:])
        return ''.join(ans)


def main():
    print(Solution().minRemoveToMakeValid('))(('))


if __name__ == '__main__':
    main()

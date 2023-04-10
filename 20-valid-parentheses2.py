"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            ']': '[',
            '}': '{',
            }
        stack = []
        for c in s:
            if c in d:
                if not stack or stack[-1] != d[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack


def main():
    print(Solution().isValid('({[]}[])'))


if __name__ == '__main__':
    main()

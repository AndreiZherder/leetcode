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

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d1 = {'(', '[', '{'}
        d2 = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in d1:
                stack.append(c)
            if c in d2:
                if not stack or stack.pop() != d2[c]:
                    return False
        return False if stack else True


def main():
    print(Solution().isValid('({[]}[])'))


if __name__ == '__main__':
    main()

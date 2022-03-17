"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2


Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            else:
                lst = stack.pop()
                stack[-1].append(2 * sum(lst) if lst else 1)
        return sum(stack[0]) if stack[0] else 1


def main():
    s = '((()))'
    print(Solution().scoreOfParentheses(s))


if __name__ == '__main__':
    main()

"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        symbols = []
        stack = [[0, 0]]
        for c in s:
            if c == '(':
                symbols.append(c)
                stack.append([0, 0])
            else:
                if symbols:
                    symbols.pop()
                    stack[-1][0] = max(stack[-1][0], stack[-1][1])
                    stack[-2][1] += stack[-1][0] + 2
                    stack.pop()
                else:
                    stack[-1][0] = max(stack[-1][0], stack[-1][1])
                    stack[-1][1] = 0
        ans = 0
        for i in range(len(stack)):
            stack[i][0] = max(stack[i][0], stack[i][1])
            ans = max(ans, stack[i][0])
        return ans


def main():
    print(Solution().longestValidParentheses('()(()'))
    # print(Solution().longestValidParentheses('()(())'))


if __name__ == '__main__':
    main()

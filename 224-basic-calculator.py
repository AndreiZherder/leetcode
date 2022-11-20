"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""
from operator import add, sub, mul
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        for token in tokens:
            if token == '±':
                stack.append(-int(stack.pop()))
            elif token in ops:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack.pop()

    def getRPN(self, s: str) -> List[str]:
        tokens = []
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i].isdigit():
                num = []
                while i < n and s[i].isdigit():
                    num.append(s[i])
                    i += 1
                tokens.append(int(''.join(num)))
                continue
            if s[i] == '(':
                stack.append('(')
                i += 1
                continue
            if s[i] == ')':
                while stack[-1] != '(':
                    tokens.append(stack.pop())
                stack.pop()
                i += 1
                continue
            if s[i] == '-' and (i == 0 or s[i - 1] in ['*', '/', '+', '-', '(']):
                stack.append('±')
                i += 1
                continue
            if s[i] in ['*', '/']:
                while stack and stack[-1] in ['*', '/', '±']:
                    tokens.append(stack.pop())
                stack.append(s[i])
                i += 1
                continue
            if s[i] in ['+', '-']:
                while stack and stack[-1] in ['*', '/', '+', '-', '±']:
                    tokens.append(stack.pop())
                stack.append(s[i])
                i += 1
                continue
            i += 1
        while stack:
            tokens.append(stack.pop())
        return tokens

    def calculate(self, s: str) -> int:
        s = ''.join(s.split())
        tokens = self.getRPN(s)
        return self.evalRPN(tokens)


def main():
    # s = "(1+(4+5+2)-3)+(6+8)"
    # s = "1 + 1"
    # s = " 2-1 + 2 "
    # s = "-2 + 1"
    # s = "(123 - 23) / 20"
    s = "-7 * -(5 + (-6)) + 7"
    print(Solution().calculate(s))


if __name__ == '__main__':
    main()

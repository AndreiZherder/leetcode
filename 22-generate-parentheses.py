"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        ans = []
        for s in self.generateParenthesis(n - 1):
            for i in range(len(s) + 1):
                ans.append(s[:i] + '()' + s[i:])
        return list(set(ans))


def main():
    n = 8
    print(Solution().generateParenthesis(n))


if __name__ == '__main__':
    main()

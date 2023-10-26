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
        def backtrack(x: int, y: int, cur: List[str]):
            if x == n:
                if y == n:
                    ans.append(''.join(cur))
                else:
                    cur.append(')')
                    backtrack(x, y + 1, cur)
                    cur.pop()
            else:
                if y < x:
                    cur.append(')')
                    backtrack(x, y + 1, cur)
                    cur.pop()
                cur.append('(')
                backtrack(x + 1, y, cur)
                cur.pop()

        ans = []
        backtrack(0, 0, [])
        return ans


def main():
    n = 3
    print(Solution().generateParenthesis(n))


if __name__ == '__main__':
    main()

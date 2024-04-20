"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]


Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(i: int, cur: List[str]):
            if i == n:
                ans.append(''.join(cur))
                return
            if s[i].isdigit():
                cur.append(s[i])
                backtrack(i + 1, cur)
                cur.pop()
            else:
                cur.append(s[i].lower())
                backtrack(i + 1, cur)
                cur.pop()
                cur.append(s[i].upper())
                backtrack(i + 1, cur)
                cur.pop()

        n = len(s)
        ans = []
        backtrack(0, [])
        return ans


def main():
    s = "a1b2"
    print(Solution().letterCasePermutation(s))


if __name__ == '__main__':
    main()

"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.



Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20


Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.

"""
from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        stack = []
        ans = 0
        if x >= y:
            c1, c2 = 'a', 'b'
        else:
            c1, c2 = 'b', 'a'
            x, y = y, x
        for c in s:
            if c == c2:
                if stack and stack[-1] == c1:
                    ans += x
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        s, stack = stack, []
        for c in s:
            if c == c1:
                if stack and stack[-1] == c2:
                    ans += y
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return ans


def main():
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(Solution().maximumGain(s, x, y))


if __name__ == '__main__':
    main()

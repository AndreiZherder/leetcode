"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""
from itertools import zip_longest


class Solution:
    def gen(self, s: str) -> str:
        cnt = 0
        for char in reversed(s):
            if char == '#':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                yield char

    def backspaceCompare(self, s: str, t: str) -> bool:
        chars1 = self.gen(s)
        chars2 = self.gen(t)
        return all(ch1 == ch2 for ch1, ch2 in zip_longest(chars1, chars2))


def main():
    s = "a#c"
    t = "b"
    print(Solution().backspaceCompare(s, t))


if __name__ == '__main__':
    main()

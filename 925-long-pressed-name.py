"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.


Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.

"""
from itertools import zip_longest, groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        for (k1, g1), (k2, g2) in zip_longest(groupby(name), groupby(typed), fillvalue=("A", "A")):
            g1 = list(g1)
            g2 = list(g2)
            if k1 != k2 or len(g1) > len(g2):
                return False
        return True


def main():
    name = "leelee"
    typed = "lleeelee"
    print(Solution().isLongPressedName(name, typed))


if __name__ == '__main__':
    main()

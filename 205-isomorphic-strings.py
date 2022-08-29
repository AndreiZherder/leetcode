"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        seen = set()
        for a, b in zip(s, t):
            if a in d:
                if d[a] != b:
                    return False
            else:
                if b in seen:
                    return False
                d[a] = b
                seen.add(b)
        return True


def main():
    # s = "paper"
    # t = "title"
    s = "foo"
    t = "bar"
    print(Solution().isIsomorphic(s, t))


if __name__ == '__main__':
    main()

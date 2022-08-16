"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                first, cnt = d[c]
                d[c] = (first, cnt + 1)
            else:
                d[c] = (i, 1)

        first, cnt = min(d.values(), key=lambda value: (value[1], value[0]))
        if cnt > 1:
            return -1
        else:
            return first


def main():
    s = "loveleetcode"
    # s = "leetcode"
    # s = "aabbcdd"
    # s = "aadadaad"
    print(Solution().firstUniqChar(s))


if __name__ == '__main__':
    main()

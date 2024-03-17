"""
You are given a string s and a character c. Return the total number of
substrings
 of s that start and end with c.



Example 1:

Input: s = "abada", c = "a"

Output: 6

Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".

Example 2:

Input: s = "zzz", c = "z"

Output: 6

Explanation: There are a total of 6 substrings in s and all start and end with "z".



Constraints:

1 <= s.length <= 105
s and c consist only of lowercase English letters.

"""


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = s.count(c)
        return n * (n + 1) // 2


def main():
    s = "abada"
    c = "a"
    print(Solution().countSubstrings(s, c))


if __name__ == '__main__':
    main()

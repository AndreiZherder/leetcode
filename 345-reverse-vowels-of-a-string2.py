"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] not in 'aeiouAEIOU':
                i += 1
                continue
            if s[j] not in 'aeiouAEIOU':
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)


def main():
    s = "leetcode"
    print(Solution().reverseVowels(s))


if __name__ == '__main__':
    main()

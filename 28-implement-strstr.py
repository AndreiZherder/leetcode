"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().



Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


Constraints:

1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def check(i : int):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    return False
            return True
        for i in range(len(haystack) - len(needle) + 1):
            if check(i):
                return i
        return -1



def main():
    haystack = "hello"
    needle = "lo"
    print(Solution().strStr(haystack, needle))


if __name__ == '__main__':
    main()

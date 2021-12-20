"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for
those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""



class Solution:
    def inner_decodeString(self, s: str):
        lst = []
        j = 0
        i = 0
        while i < len(s):
            if s[i] == ']':
                lst.append(s[j:i])
                return ''.join(lst), i
            if s[i].isdigit():
                lst.append(s[j:i])
                j = i
                while s[i] != '[':
                    i += 1
                n = int(s[j:i])
                i += 1
                j = i
                substr, length = self.inner_decodeString(s[i:])
                for k in range(n):
                    lst.append(substr)
                i += length
                j += length + 1
            i += 1
        lst.append(s[j:i])
        return ''.join(lst), i

    def decodeString(self, s: str) -> str:
        ans, _ = self.inner_decodeString(s)
        return ans


def main():
    # s = "3[a]2[bc]"
    # s = "3[a2[c]]"
    # s = "2[abc]3[cd]ef"
    s = "abc3[cd]xyz"
    solution = Solution()
    print(solution.decodeString(s))


if __name__ == '__main__':
    main()

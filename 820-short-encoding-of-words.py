"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including)
the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.



Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
Example 2:

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].


Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = (dict(), 0)
        trie[0]['dummy'] = (dict(), 1)
        cnt1 = 0
        cnt2 = 0
        for word in words:
            d, level = trie
            for c in reversed(word):
                if c not in d:
                    if d:
                        cnt2 += 1
                        cnt1 += level
                    cnt1 += 1
                    d[c] = (dict(), level + 1)
                d, level = d[c]
        return cnt1 + cnt2


def main():
    # words = ["time", "me", "bell"]
    # words = ["t"]
    words = ["time", "atime", "btime"]
    print(Solution().minimumLengthEncoding(words))


if __name__ == '__main__':
    main()

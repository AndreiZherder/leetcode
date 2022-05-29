"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. If no such two words exist, return 0.



Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""
from typing import List


class Solution:
    mapping = {
        'a': 0x00000001,
        'b': 0x00000002,
        'c': 0x00000004,
        'd': 0x00000008,
        'e': 0x00000010,
        'f': 0x00000020,
        'g': 0x00000040,
        'h': 0x00000080,
        'i': 0x00000100,
        'j': 0x00000200,
        'k': 0x00000400,
        'l': 0x00000800,
        'm': 0x00001000,
        'n': 0x00002000,
        'o': 0x00004000,
        'p': 0x00008000,
        'q': 0x00010000,
        'r': 0x00020000,
        's': 0x00040000,
        't': 0x00080000,
        'u': 0x00100000,
        'v': 0x00200000,
        'w': 0x00400000,
        'x': 0x00800000,
        'y': 0x01000000,
        'z': 0x02000000,
    }

    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0 for i in range(n)]
        for i, word in enumerate(words):
            for letter in word:
                masks[i] |= self.mapping[letter]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


def main():
    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    print(Solution().maxProduct(words))


if __name__ == '__main__':
    main()

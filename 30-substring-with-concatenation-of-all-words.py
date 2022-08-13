"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s)
in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def compare_words(i: int):
            count = Counter(words)
            for j in range(i, i + length, word_length):
                word = s[j:j + word_length]
                if word not in count:
                    break
                else:
                    count[word] -= 1
                    if count[word] == 0:
                        del count[word]
            else:
                ans.append(i)

        ans = []
        word_length = len(words[0])
        length = len(words) * word_length
        pattern = Counter()
        for word in words:
            for c in word:
                pattern[c] += 1
        count = Counter(s[:length])
        if count == pattern:
            compare_words(0)
        for i in range(1, len(s) - length + 1):
            count[s[i - 1]] -= 1
            if count[s[i - 1]] == 0:
                del count[s[i - 1]]
            count[s[i + length - 1]] += 1
            if count == pattern:
                compare_words(i)
        return ans


def main():
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "good"]
    print(Solution().findSubstring(s, words))


if __name__ == '__main__':
    main()

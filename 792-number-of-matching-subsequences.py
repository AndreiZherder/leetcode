"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        ans = 0
        for word in words:
            j = -1
            for c in word:
                if c in d:
                    i = bisect_right(d[c], j)
                    if i == len(d[c]):
                        break
                    else:
                        j = d[c][i]
                else:
                    break
            else:
                ans += 1
        return ans


def main():
    # s = "abcde"
    # words = ["a", "bb", "acd", "ace"]
    # s = "dsahjpjauf"
    # words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    s = "dsahjpjauf"
    words = ["jaa"]
    print(Solution().numMatchingSubseq(s, words))


if __name__ == '__main__':
    main()

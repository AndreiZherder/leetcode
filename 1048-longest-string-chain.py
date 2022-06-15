"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA
without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on.
A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List


class Solution:
    def chain_between(self, word1: str, word2: str) -> bool:
        j = 0
        i = 0
        cnt = 0
        while i < len(word1):
            if word2[j] == word1[i]:
                i += 1
                j += 1
            else:
                if cnt == 1:
                    return False
                cnt += 1
                j += 1
        return True

    def longestStrChain(self, words: List[str]) -> int:
        ans = 1
        d = defaultdict(dict)
        for word in words:
            d[len(word)][word] = 1
        for word1_length in sorted(d):
            for word1, chain_length1 in d[word1_length].items():
                for word2, chain_length2 in d[word1_length + 1].items():
                    if self.chain_between(word1, word2):
                        chain_length2 = max(chain_length2, chain_length1 + 1)
                        d[word1_length + 1][word2] = chain_length2
                        ans = max(ans, chain_length2)
        return ans


def main():
    words = ["abcd", "dbqca"]
    print(Solution().longestStrChain(words))


if __name__ == '__main__':
    main()

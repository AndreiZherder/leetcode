"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.



Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]


Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 10^5
"""
from functools import lru_cache
from itertools import chain
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def add_to_trie(trie: dict, word: str):
            node = trie
            for c in chain(word, '#'):
                if c not in node:
                    node[c] = dict()
                node = node[c]

        @lru_cache(None)
        def dfs(word: str, i: int) -> bool:
            if i == len(word):
                return True
            node = trie
            for j in range(i, len(word)):
                if word[j] not in node:
                    return False
                if '#' in node[word[j]] and dfs(word, j + 1):
                    return True
                node = node[word[j]]
            return False

        trie = dict()
        words.sort(key=len)
        ans = []
        for word in words:
            if dfs(word, 0):
                ans.append(word)
            else:
                add_to_trie(trie, word)
        return ans


def main():
    # words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    words = ["cat", "dog", "catdog"]
    print(Solution().findAllConcatenatedWordsInADict(words))


if __name__ == '__main__':
    main()

"""
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from functools import lru_cache
from typing import List


class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["_end_"] = {}

    def __contains__(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "_end_" in node

    def startswith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def dp(i: int) -> bool:
            if i == n:
                return True
            for j in range(i, n):
                if s[i:j + 1] in trie and dp(j + 1):
                    return True
            return False

        trie = Trie()
        for word in wordDict:
            trie.add(word)
        n = len(s)
        return dp(0)


def main():
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict))


if __name__ == '__main__':
    main()

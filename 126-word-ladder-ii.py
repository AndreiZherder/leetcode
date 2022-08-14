"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList,
return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.
Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        @lru_cache(None)
        def dfs(word: str) -> List[List[str]]:
            if word == beginWord:
                return [[beginWord]]
            else:
                ans = []
                for parent in tree[word]:
                    for path in dfs(parent):
                        ans.append([word] + path)
                return ans

        d = set(wordList)
        d.discard(beginWord)
        if endWord not in d:
            return []
        q, q1 = set(), set()
        tree = defaultdict(list)
        q.add(beginWord)
        found = False
        while q:
            seen_on_level = set()
            while q:
                word = q.pop()
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = ''.join((word[:i], j, word[i + 1:]))
                        if new_word in d:
                            if new_word != endWord:
                                q1.add(new_word)
                            else:
                                found = True
                            tree[new_word].append(word)
                            seen_on_level.add(new_word)
            d -= seen_on_level
            q, q1 = q1, q

            if found:
                ans = dfs(endWord)
                return [path[::-1] for path in ans]


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))


if __name__ == '__main__':
    main()

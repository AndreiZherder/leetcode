"""
In English, we have a concept called root, which can be followed by some other word to form another longer word
et's call this word derivative. For example, when the root "help" is followed by the word "ful",
we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by
more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.



Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.

"""
from typing import List


class Trie:
    def __init__(self, words):
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
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        trie = Trie(dictionary)
        for word in sentence.split():
            node = trie.root
            ok = False
            for i, c in enumerate(word):
                if c in node:
                    node = node[c]
                    if '_end_' in node:
                        ans.append(word[:i + 1])
                        ok = True
                        break
                else:
                    ans.append(word)
                    ok = True
                    break
            if not ok:
                ans.append(word)
        return ' '.join(ans)



def main():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary, sentence))


if __name__ == '__main__':
    main()

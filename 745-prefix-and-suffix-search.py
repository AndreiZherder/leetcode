"""
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary,
which has the prefix prefix and the suffix suffix.
If there is more than one valid index, return the largest of them.
If there is no such word in the dictionary, return -1.


Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".


Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
"""
from bisect import bisect_right
from collections import defaultdict
from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.d1 = defaultdict(list)
        self.d2 = defaultdict(list)
        for i, word in enumerate(words):
            for j in range(len(word)):
                self.d1[word[:j + 1]].append(i)
                self.d2[word[len(word) - 1 - j:]].append(i)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.d1.get(prefix, [])
        b = self.d2.get(suffix, [])
        if not a:
            return -1
        if not b:
            return -1
        j = bisect_right(b, a[-1]) - 1
        for num in reversed(a):
            while j >= 0 and b[j] > num:
                j -= 1
            if j >= 0 and b[j] == num:
                return num
        return -1


def main():
    wordFilter = WordFilter(["bbbb", "bbbb", "abbc"])
    print(wordFilter.f("a", "b"))
    print(wordFilter.f("ap", "es"))
    print(wordFilter.f("app", "s"))
    print(wordFilter.f("app", "q"))


if __name__ == '__main__':
    main()

"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.



Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]


Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""
from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def match(word: str):
            d = Counter(word)
            for char, cnt in pattern.items():
                if d.get(char, 0) < cnt:
                    return False
            return True

        pattern = Counter()
        for word in words2:
            for char, cnt in Counter(word).items():
                pattern[char] = max(pattern[char], cnt)
        return list(filter(match, words1))


def main():
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "oo"]
    print(Solution().wordSubsets(words1, words2))


if __name__ == '__main__':
    main()

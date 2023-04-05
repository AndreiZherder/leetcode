"""
Given a string s and a string array dictionary, return the longest string in the dictionary
that can be formed by deleting some of the given string characters.
If there is more than one possible result, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.



Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"


Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = -1
            for c in word:
                i = s.find(c, i + 1)
                if i == -1:
                    break
            else:
                return word
        return ''


def main():
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    print(Solution().findLongestWord(s, dictionary))


if __name__ == '__main__':
    main()

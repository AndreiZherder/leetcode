"""
You are given a 0-indexed string word, consisting of lowercase English letters.
You need to select one index and remove the letter at that index from word so that the frequency of every
letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal,
and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.


Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2,
or vice versa. It is impossible to make all present letters have equal frequency.


Constraints:

2 <= word.length <= 100
word consists of lowercase English letters only.

"""
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        if len(c) == 1:
            return True
        mx = max(c.values())
        mn = min(c.values())
        if all(v == 1 for v in c.values()):
            return True
        if all(v == mx - 1 for v in c.values() if v != mx) and Counter(c.values())[mx] == 1:
            return True
        if mn == 1 and all(v == mx for v in c.values() if v != mn) and Counter(c.values())[mn] == 1:
            return True
        return False



def main():
    word = "abcc"
    print(Solution().equalFrequency(word))


if __name__ == '__main__':
    main()

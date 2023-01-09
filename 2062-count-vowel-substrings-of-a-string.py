"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u')
and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"


Constraints:

1 <= word.length <= 100
word consists of lowercase English letters only.
"""
from collections import Counter


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        n = len(word)
        for i in range(5, n + 1):
            c = Counter(word[:i])
            if len(c) == 5 and all(char in 'aeiou' for char in c):
                ans += 1
            for j in range(1, n - i + 1):
                c[word[j - 1]] -= 1
                if c[word[j - 1]] == 0:
                    del c[word[j - 1]]
                c[word[j + i - 1]] += 1
                if len(c) == 5 and all(char in 'aeiou' for char in c):
                    ans += 1
        return ans


def main():
    word = "cuaieuouac"
    print(Solution().countVowelSubstrings(word))


if __name__ == '__main__':
    main()

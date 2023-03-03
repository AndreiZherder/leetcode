"""
Given an array of strings patterns and a string word, return the number of strings in patterns that exist
as a substring in word.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
Example 2:

Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.
Example 3:

Input: patterns = ["a","a","a"], word = "ab"
Output: 3
Explanation: Each of the patterns appears as a substring in word "ab".


Constraints:

1 <= patterns.length <= 100
1 <= patterns[i].length <= 100
1 <= word.length <= 100
patterns[i] and word consist of lowercase English letters.
"""
from typing import List

# https://github.com/TheAlgorithms/Python/blob/master/strings/rabin_karp.py

# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 1000003
def rabin_karp(pattern: str, text: str) -> int:
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return -1

    p_hash = 0
    text_hash = 0
    modulus_power = 1

    # Calculating the hash of pattern and substring of text
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(0, t_len - p_len + 1):
        if text_hash == p_hash and text[i : i + p_len] == pattern:
            return i
        if i == t_len - p_len:
            continue
        # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
        text_hash = (
            (text_hash - ord(text[i]) * modulus_power) * alphabet_size
            + ord(text[i + p_len])
        ) % modulus
    return -1

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(rabin_karp(pattern, word) != -1 for pattern in patterns)


def main():
    patterns = ["a", "b", "c"]
    word = "aaaaabbbbb"
    print(Solution().numOfStrings(patterns, word))


if __name__ == '__main__':
    main()

"""
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word,
and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.



Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.



Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.

"""
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for c1, c2 in zip(ascii_lowercase, ascii_uppercase):
            if c1 in word and c2 in word and word.rfind(c1) < word.find(c2):
                ans += 1
        return ans


def main():
    word = "abBCab"
    print(Solution().numberOfSpecialChars(word))


if __name__ == '__main__':
    main()

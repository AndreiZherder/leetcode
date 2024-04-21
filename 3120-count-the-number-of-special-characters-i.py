"""
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.



Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.



Constraints:

1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.

"""
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for c1, c2 in zip(ascii_lowercase, ascii_uppercase):
            if c1 in word and c2 in word:
                ans += 1
        return ans


def main():
    word = "abBCab"
    print(Solution().numberOfSpecialChars(word))


if __name__ == '__main__':
    main()

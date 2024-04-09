"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'),
punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken
down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters
("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token
("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.



Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".
Example 2:

Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.
Example 3:

Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.


Constraints:

1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.

"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        for word in sentence.split():
            if any(c.isdigit() for c in word):
                continue
            cnt = word.count('-')
            if cnt > 1:
                continue
            if cnt == 1:
                i = word.find('-')
                if i < 1 or i == len(word) - 1 or not word[i - 1].isalpha() or not word[i + 1].isalpha():
                    continue
            cnt = 0
            for c in word:
                if c in '!.,':
                    cnt += 1
            if cnt > 1:
                continue
            if cnt == 1:
                if word[-1] not in '!.,':
                    continue
            ans += 1
        return ans


def main():
    sentence = "!this  1-s b8d!"
    print(Solution().countValidWords(sentence))


if __name__ == '__main__':
    main()

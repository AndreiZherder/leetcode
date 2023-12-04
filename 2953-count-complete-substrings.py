"""
You are given a string word and an integer k.

A substring s of word is complete if:

Each character in s occurs exactly k times.
The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s,
the absolute difference in their positions in the alphabet is at most 2.
Return the number of complete substrings of word.

A substring is a non-empty contiguous sequence of characters in a string.



Example 1:

Input: word = "igigee", k = 2
Output: 3
Explanation: The complete substrings where each character appears exactly twice and the difference between
adjacent characters is at most 2 are: igigee, igigee, igigee.
Example 2:

Input: word = "aaabbbccc", k = 3
Output: 6
Explanation: The complete substrings where each character appears exactly three times and the difference
between adjacent characters is at most 2 are: aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc.


Constraints:

1 <= word.length <= 105
word consists only of lowercase English letters.
1 <= k <= word.length

"""
from collections import Counter
from typing import List


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        words = []
        begin = 0
        for i in range(1, n):
            if abs(ord(word[i]) - ord(word[i - 1])) > 2:
                words.append(word[begin:i])
                begin = i
        words.append(word[begin:])
        ans = 0
        for l in range(1, 27):
            win_len = l * k
            for word in words:
                m = len(word)
                if m < win_len:
                    continue
                counter = Counter(word[:win_len])
                if all(v == k for v in counter.values()):
                    ans += 1
                for i in range(win_len, m):
                    counter[word[i]] += 1
                    counter[word[i - win_len]] -= 1
                    if counter[word[i - win_len]] == 0:
                        del counter[word[i - win_len]]
                    if all(v == k for v in counter.values()):
                        ans += 1
        return ans


def main():
    word = "igigee"
    k = 2
    print(Solution().countCompleteSubstrings(word, k))


if __name__ == '__main__':
    main()

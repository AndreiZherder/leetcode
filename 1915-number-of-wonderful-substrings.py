"""
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word,
then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"


Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.

"""
from collections import Counter
from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def subarray_sum_k(pref: List[int], k: int) -> int:
            d = Counter({0: 1})
            ans = 0
            for num in pref:
                ans += d[num ^ k]
                d[num] += 1
            return ans
        pref = list(accumulate((1 << (ord(c) - ord('a')) for c in word), xor))
        ans = subarray_sum_k(pref, 0)
        for j in range(10):
            ans += subarray_sum_k(pref, 1 << j)
        return ans


def main():
    word = "aba"
    print(Solution().wonderfulSubstrings(word))


if __name__ == '__main__':
    main()

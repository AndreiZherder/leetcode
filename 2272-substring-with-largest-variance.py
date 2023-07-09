"""
The variance of a string is defined as the largest difference between the number of occurrences of any 2
characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only,
return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
from collections import Counter
from itertools import product


class Solution:
    def largestVariance(self, s: str) -> int:
        def kadane(x: str, y: str) -> int:
            if x == y:
                return 0
            best = 0
            x_cnt = 0
            y_cnt = 0
            rest_y = cnt[y]
            for c in s:
                if c == x:
                    x_cnt += 1
                elif c == y:
                    y_cnt += 1
                    rest_y -= 1
                else:
                    continue
                if y_cnt > 0:
                    best = max(best, x_cnt - y_cnt)
                if y_cnt > x_cnt and rest_y:
                    x_cnt = 0
                    y_cnt = 0
            return best

        cnt = Counter(s)
        return max((kadane(x, y) for x, y in product(list(set(s)), repeat=2)), default=0)


def main():
    s = "aababbb"
    print(Solution().largestVariance(s))


if __name__ == '__main__':
    main()

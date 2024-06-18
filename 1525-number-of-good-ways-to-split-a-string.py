"""
You are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation
is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.



Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""
from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        counter1 = Counter()
        counter2 = Counter(s)
        ans = 0
        for c in s:
            counter1[c] += 1
            counter2[c] -= 1
            if counter2[c] == 0:
                del counter2[c]
            if len(counter1) == len(counter2):
                ans += 1
        return ans


def main():
    s = "aacaba"
    print(Solution().numSplits(s))


if __name__ == '__main__':
    main()

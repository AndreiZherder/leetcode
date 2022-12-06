"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b'
in the string. Otherwise, return false.



Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.


Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.
"""


class Solution:
    def checkString(self, s: str) -> bool:
        ans = True
        n = len(s)
        first_b_pos = s.find('b')
        if first_b_pos == -1:
            return True
        last_a_pos = n - s[::-1].find('a') - 1
        if last_a_pos == n:
            return True
        return last_a_pos < first_b_pos


def main():
    s = "abab"
    print(Solution().checkString(s))


if __name__ == '__main__':
    main()

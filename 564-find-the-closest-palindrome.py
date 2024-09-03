"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome.
If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.



Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.


Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].

"""
from typing import List


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)
        s = {10 ** (length - 1) - 1, 10 ** length + 1}
        pref = int(n[:(length + 1) // 2])

        for i in range(pref - 1, pref + 2):
            j = i if length % 2 == 0 else i // 10
            cur = i
            while j > 0:
                cur = cur * 10 + j % 10
                j //= 10
            s.add(cur)
        s.discard(num)
        cur = -1
        for c in s:
            if cur == -1 or abs(c - num) < abs(cur - num) or (abs(c - num) == abs(cur - num) and c < cur):
                cur = c
        return str(cur)


def main():
    n = "123"
    print(Solution().nearestPalindromic(n))


if __name__ == '__main__':
    main()

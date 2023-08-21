"""
Given a string s, check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""


def prime_factors(n: int):
    """
    Prime factors of n
    prime_factors(99) --> 3 3 11
    """
    while n % 2 == 0:
        yield 2
        n //= 2
    p = 3
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            n = quotient
        else:
            p += 2
    if n != 1:
        yield n


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        pf = set(prime_factors(n))
        return(any(s[:n // p] * p == s for p in pf))


def main():
    s = "abcabcabcabc"
    print(Solution().repeatedSubstringPattern(s))


if __name__ == '__main__':
    main()

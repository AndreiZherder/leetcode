"""
You are given a string s, which is known to be a concatenation of anagrams of some string t.

Return the minimum possible length of the string t.

An anagram is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".



Example 1:

Input: s = "abba"

Output: 2

Explanation:

One possible string t could be "ba".

Example 2:

Input: s = "cdef"

Output: 4

Explanation:

One possible string t could be "cdef", notice that t can be equal to s.



Constraints:

1 <= s.length <= 105
s consist only of lowercase English letters.

"""
from collections import Counter
from typing import List


def factors(n: int):
    """
    Distinct factors of n
    """
    stack = []
    yield 1
    if n != 1:
        stack.append(n)
    p = 2
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            if quotient != p:
                stack.append(quotient)
        p += 1
    while stack:
        yield stack.pop()



class Solution:
    def minAnagramLength(self, s: str) -> int:
        def check(k: int) -> bool:
            target = Counter(s[:k])
            return all(Counter(s[i:i + k]) == target for i in range(0, n, k))
        n = len(s)
        for f in reversed(list(factors(n))):
            if check(n // f):
                return n // f


def main():
    s = "abba"
    print(Solution().minAnagramLength(s))


if __name__ == '__main__':
    main()

"""
You are given 2 positive integers l and r. For any number x, all positive divisors of x except x are called the proper
divisors of x.

A number is called special if it has exactly 2 proper divisors. For example:

The number 4 is special because it has proper divisors 1 and 2.
The number 6 is not special because it has proper divisors 1, 2, and 3.
Return the count of numbers in the range [l, r] that are not special.



Example 1:

Input: l = 5, r = 7

Output: 3

Explanation:

There are no special numbers in the range [5, 7].

Example 2:

Input: l = 4, r = 16

Output: 11

Explanation:

The special numbers in the range [4, 16] are 4 and 9.



Constraints:

1 <= l <= r <= 109

"""
from math import isqrt


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def sieve(n: int):
            """
            Primes <= n
            """
            primes = bytearray(n + 1)
            p = 3
            while p * p <= n:
                if not primes[p]:
                    primes[p * p::p] = [1] * len(primes[p * p::p])
                p += 2
            if n >= 2:
                yield 2
            for p in range(3, n + 1, 2):
                if not primes[p]:
                    yield p

        return r - l + 1 - (len(list(sieve(isqrt(r)))) - len(list(sieve(isqrt(l - 1)))))


def main():
    l = 4
    r = 16
    print(Solution().nonSpecialCount(l, r))


if __name__ == '__main__':
    main()

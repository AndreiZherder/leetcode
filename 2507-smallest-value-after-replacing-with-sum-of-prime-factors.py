"""
You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.



Example 1:

Input: n = 15
Output: 5
Explanation: Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.
Example 2:

Input: n = 3
Output: 3
Explanation: Initially, n = 3.
3 is the smallest value n will take on.


Constraints:

2 <= n <= 10^5
"""


class Solution:
    def smallestValue(self, n: int) -> int:

        def prime_factors(n):
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

        s = sum(prime_factors(n))
        while s != n:
            n = s
            s = sum(prime_factors(n))
        return n


def main():
    n = 15
    print(Solution().smallestValue(n))


if __name__ == '__main__':
    main()

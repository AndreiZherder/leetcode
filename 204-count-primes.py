"""
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 10^6
"""


class Solution:
    def countPrimes(self, n: int) -> int:

        def sieve(n: int):
            cnt = 0
            if n >= 2:
                cnt += 1
            primes = bytearray(n + 1)
            p = 3
            while p * p <= n:
                if not primes[p]:
                    primes[p * p::p] = [1] * len(primes[p * p::p])
                p += 2
            for p in range(3, n + 1, 2):
                if not primes[p]:
                    cnt += 1
            return cnt

        return sieve(n - 1)


def main():
    n = 5 * 10 ** 6
    print(Solution().countPrimes(n))


if __name__ == '__main__':
    main()

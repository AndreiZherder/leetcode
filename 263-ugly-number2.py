"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.



Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.


Constraints:

-2^31 <= n <= 2^31 - 1
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for num in [5, 3, 2]:
            while n % num == 0:
                n //= num
        return n == 1


def main():
    n = 90
    print(Solution().isUgly(n))


if __name__ == '__main__':
    main()

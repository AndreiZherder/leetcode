"""
You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on
an infinite number line. With one step, you can move either one position to the left, or one position to the right.

Given a positive integer k, return the number of different ways to reach the position endPos starting
from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.

Two ways are considered different if the order of the steps made is not exactly the same.

Note that the number line includes negative integers.



Example 1:

Input: startPos = 1, endPos = 2, k = 3
Output: 3
Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.
Example 2:

Input: startPos = 2, endPos = 5, k = 10
Output: 0
Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.


Constraints:

1 <= startPos, endPos, k <= 1000

"""
from typing import Tuple

mod = 10 ** 9 + 7


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Given two integers a and b, returns (gcd(a, b), x, y) such that
    a * x + b * y == gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def mmul(x: int, y: int) -> int:
    return (x * y) % mod


def minv(x: int) -> int:
    """
    returns modular inverse of x when mod is prime or not prime
    ans = (1 / x) % mod
    gcd(y, mod) should be 1
    """
    g, inv, _ = egcd(x, mod)
    if g != 1:
        raise ValueError('gcd(x, mod) != 1')
    return inv % mod


def mdiv(x: int, y: int) -> int:
    """
    returns (x / y) % mod
    gcd(y, mod) should be 1
    """
    return (x * minv(y)) % mod


def ncr(n: int, r: int) -> int:
    """
    returns number of ways for selecting r elements out of n options
    """
    num, den = 1, 1
    for i in range(r):
        num = mmul(num, n - i)
        den = mmul(den, i + 1)
    return mdiv(num, den)


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if abs(endPos - startPos) > k or (k - abs(endPos - startPos)) % 2 == 1:
            return 0
        return ncr(k, (k - abs(endPos - startPos)) // 2)


def main():
    startPos = 1
    endPos = 2
    k = 3
    print(Solution().numberOfWays(startPos, endPos, k))


if __name__ == '__main__':
    main()

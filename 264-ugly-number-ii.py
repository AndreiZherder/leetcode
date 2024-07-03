"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:

1 <= n <= 1690

"""
from sortedcontainers import SortedSet


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = SortedSet((1, 2, 3, 5))
        i = 0
        cur = s[i]
        while i < n:
            for f in (2, 3, 5):
                s.add(cur * f)
            i += 1
            cur = s[i]
        return s[n - 1]


def main():
    n = 10
    print(Solution().nthUglyNumber(n))


if __name__ == '__main__':
    main()

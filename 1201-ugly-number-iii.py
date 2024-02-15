"""
An ugly number is a positive integer that is divisible by a, b, or c.

Given four integers n, a, b, and c, return the nth ugly number.



Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.


Constraints:

1 <= n, a, b, c <= 109
1 <= a * b * c <= 1018
It is guaranteed that the result will be in range [1, 2 * 109].

"""


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def bsl(left: int, right: int) -> int:
            """
            FFFFTTTT
                |
            """
            def check(mid: int) -> bool:
                return mid // a + mid // b + mid // c - mid // lcm(a, b) - mid // lcm(a, c) - mid // lcm(b, c) + mid // lcm(a,  b,  c) >= n

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        return bsl(min(a, b, c), 2 * 10 ** 9)


def main():
    n = 4
    a = 2
    b = 3
    c = 4
    print(Solution().nthUglyNumber(n, a, b, c))


if __name__ == '__main__':
    main()

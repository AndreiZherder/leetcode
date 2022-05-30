"""
Given two integers dividend and divisor, divide two integers without using multiplication, division,
and mod operator.

The integer division should truncate toward zero, which means losing its fractional part.
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
[−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,
and if the quotient is strictly less than -2^31, then return -2^31.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        dividend_sign = dividend > 0
        divisor_sign = divisor > 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        i = 31  # Cheating. In 32-bits this solution is not possible
        mask = 0x80000000
        while not mask & dividend:
            i -= 1
            mask >>= 1
        quotient = 0
        a = 1
        while i >= 0:
            if a < divisor:
                quotient <<= 1
                if i > 0:
                    a = (a << 1) + ((dividend >> (i - 1)) & 0x00000001)
            else:
                quotient = (quotient << 1) + 1
                if i > 0:
                    a = ((a - divisor) << 1) + ((dividend >> (i - 1)) & 0x00000001)
            i -= 1
        if (dividend_sign and not divisor_sign) or (not dividend_sign and divisor_sign):
            quotient = -quotient
        return quotient


def main():
    dividend = -2 ** 31
    divisor = -1
    print(Solution().divide(dividend, divisor))


if __name__ == '__main__':
    main()

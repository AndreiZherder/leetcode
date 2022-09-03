"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-2^31 <= x <= 2^31 - 1
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        digits = []
        x = abs(x)
        while x != 0:
            digits.append(x % 10)
            x //= 10
        ans = 0
        base = 1
        if sign == 1:
            for num in reversed(digits):
                add = base * num
                if 0x7FFFFFFF - add >= ans:
                    ans += add
                    base *= 10
                else:
                    return 0
        else:
            for num in reversed(digits):
                add = base * num
                if -2147483648 + add <= ans:
                    ans -= add
                    base *= 10
                else:
                    return 0
        return ans


def main():
    x = -123
    print(Solution().reverse(x))


if __name__ == '__main__':
    main()

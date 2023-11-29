"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

"""
from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ans = []
        for x, y in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            carry, cur = divmod(int(x) + int(y) + carry, 10)
            ans.append(str(cur))
        if carry:
            ans.append(str(carry))
        return ''.join(reversed(ans))


def main():
    num1 = "11"
    num2 = "123"
    print(Solution().addStrings(num1, num2))


if __name__ == '__main__':
    main()

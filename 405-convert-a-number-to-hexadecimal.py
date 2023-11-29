"""
Given an integer num, return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.



Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"


Constraints:

-231 <= num <= 231 - 1

"""
from typing import List


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        a = '0123456789abcdef'
        if num > 0:
            ans = []
            while num > 0:
                ans.append(a[num % 16])
                num //= 16
        else:
            num = 2 ** 32 + num
            ans = []
            while num > 0:
                ans.append(a[num % 16])
                num //= 16
        return ''.join(ans[::-1])



def main():
    num = -1
    print(Solution().toHex(num))


if __name__ == '__main__':
    main()

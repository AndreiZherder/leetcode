"""
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.



Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.


Constraints:

1 <= num1, num2 <= 109

"""
from typing import List


def popcount(n: int) -> int:
    """
    Count set bits in an integer
    """
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = popcount(num2)
        ans = 0
        for j in range(31, -1, -1):
            if num1 & 1 << j:
                ans |= 1 << j
                n -= 1
            if n == 0:
                break
        if n > 0:
            for j in range(32):
                if num1 & 1 << j == 0:
                    ans |= 1 << j
                    n -= 1
                if n == 0:
                    break
        return ans


def main():
    num1 = 1
    num2 = 12
    print(Solution().minimizeXor(num1, num2))


if __name__ == '__main__':
    main()

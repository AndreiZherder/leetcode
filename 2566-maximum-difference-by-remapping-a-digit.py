"""
You are given an integer num. You know that Danny Mittal will sneakily remap one of the 10 possible digits (0 to 9)
to another digit.

Return the difference between the maximum and minimum values Danny can make by remapping exactly one digit in num.

Notes:

When Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of d1 in num with d2.
Danny can remap a digit to itself, in which case num does not change.
Danny can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
We mentioned "Danny Mittal" to congratulate him on being in the top 10 in Weekly Contest 326.


Example 1:

Input: num = 11891
Output: 99009
Explanation:
To achieve the maximum value, Danny can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Danny can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be
returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.


Constraints:

1 <= num <= 10^8
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits1 = [int(digit) for digit in str(num)]
        digits2 = digits1.copy()
        n = len(digits1)

        a = -1
        for i in range(n):
            if digits1[i] == a:
                digits1[i] = 9
                continue
            if a == -1 and digits1[i] < 9:
                a = digits1[i]
                digits1[i] = 9

        a = -1
        for i in range(n):
            if digits2[i] == a:
                digits2[i] = 0
                continue
            if a == -1 and digits2[i] > 0:
                a = digits2[i]
                digits2[i] = 0

        return int(''.join(str(digit) for digit in digits1)) - int(''.join(str(digit) for digit in digits2))


def main():
    num = 11891
    print(Solution().minMaxDifference(num))


if __name__ == '__main__':
    main()

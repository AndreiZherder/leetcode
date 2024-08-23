"""
Given a string expression representing an expression of fraction addition and subtraction,
return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer,
change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.



Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"


Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator.
If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator
of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually
an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

"""
from functools import reduce
from math import gcd
from typing import List


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)
        numerators = []
        denominators = []
        words = expression.split('/')
        numerators.append(int(words[0]))
        for word in words[1:len(words) - 1]:
            nums = word.split('+')
            if len(nums) > 1:
                denominators.append(int(nums[0]))
                numerators.append(int(nums[-1]))
            else:
                nums = word.split('-')
                denominators.append(int(nums[0]))
                numerators.append(-int(nums[-1]))
        denominators.append(int(words[-1]))
        denominator = reduce(lcm, denominators)
        numerator = 0
        for d, n in zip(denominators, numerators):
            numerator += denominator // d * n
        g = gcd(numerator, denominator)
        denominator //= g
        numerator //= g
        return f'{numerator}/{denominator}'



def main():
    expression = "1/3-1/2"
    print(Solution().fractionAddition(expression))


if __name__ == '__main__':
    main()

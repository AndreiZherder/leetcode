"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""
from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        terms = []
        for i, digit in enumerate(num2[::-1]):
            terms.append(self.get_term(num1, int(digit), i))
        return self.add_terms(terms)

    def get_term(self, num1: str, multiplier: int, multiplier_pos: int) -> str:
        term = ''
        carry = 0
        for digit in num1[::-1]:
            product = int(digit) * multiplier + carry
            carry = product // 10
            term = str(product % 10) + term
        if carry:
            term = str(carry) + term
        term += '0' * multiplier_pos
        return term

    def add_terms(self, terms: List[str]) -> str:
        sum = ''
        carry = 0
        for i in range(len(terms[-1])):
            sum_of_digits = 0
            for term in terms:
                if len(term) > i:
                    sum_of_digits += int(term[-1 - i])
            sum_of_digits += carry
            carry = sum_of_digits // 10
            sum = str(sum_of_digits % 10) + sum
        if carry:
            sum = str(carry) + sum
        return sum


num1 = '0'
num2 = '9133'
print(Solution().multiply(num1, num2))

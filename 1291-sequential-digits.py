"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""
import itertools
from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        power = 0
        left_digit = low
        digits = deque()
        digits.appendleft(left_digit % 10)
        while left_digit >= 10:
            left_digit //= 10
            digits.appendleft(left_digit % 10)
            power += 1
        for i in range(1, len(digits)):
            if digits[i] - digits[i - 1] < 1:
                break
            elif digits[i] - digits[i - 1] > 1:
                left_digit += 1
                break
        if left_digit > 9 - power:
            left_digit = 1
            power += 1

        ans = list(itertools.takewhile(lambda num: num <= high, self.gen(left_digit, power)))
        return ans

    def gen(self, left_digit: int, power: int):
        while power < 9:
            while left_digit <= 9 - power:
                k = 0
                ans = 0
                while k <= power:
                    ans += (left_digit + k) * 10 ** (power - k)
                    k += 1
                yield ans
                left_digit += 1
            power += 1
            left_digit = 1


def main():
    print(*Solution().sequentialDigits(352, 1000))


if __name__ == '__main__':
    main()

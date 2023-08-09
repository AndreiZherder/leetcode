"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false


Constraints:

0 <= c <= 231 - 1

"""
from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        x = 0
        while x <= c:
            if isqrt(c - x) ** 2 == c - x:
                return True
            a += 1
            x = a * a
        return False


def main():
    c = 5
    print(Solution().judgeSquareSum(c))


if __name__ == '__main__':
    main()

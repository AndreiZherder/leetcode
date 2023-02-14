"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        for x, y in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            carry, res = divmod((int(x) + int(y) + carry), 2)
            ans.append(str(res))
        if carry:
            ans.append(str(carry))
        return ''.join(ans[::-1])


def main():
    solution = Solution()
    print(solution.addBinary('1010', '1011'))


if __name__ == '__main__':
    main()

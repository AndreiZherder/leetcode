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


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            first = int(a[i]) if i >= 0 else 0
            second = int(b[j]) if j >= 0 else 0
            sum = first + second + carry
            carry = sum >> 1
            ans.append(str(sum & 1))
            i -= 1
            j -= 1
        if carry:
            ans.append(str(carry))
        return ''.join(reversed(ans))


def main():
    solution = Solution()
    print(solution.addBinary('1010', '1011'))


if __name__ == '__main__':
    main()

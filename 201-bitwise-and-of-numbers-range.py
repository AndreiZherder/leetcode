"""
Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0


Constraints:

0 <= left <= right <= 231 - 1

"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for j in range(31, -1, -1):
            if (left & 1 << j) ^ (right & 1 << j):
                break
            if left & 1 << j == right & 1 << j == 1 << j:
                ans |= 1 << j
        return ans


def main():
    left = 5
    right = 7
    print(Solution().rangeBitwiseAnd(left, right))


if __name__ == '__main__':
    main()

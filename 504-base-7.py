"""
Given an integer num, return a string of its base 7 representation.



Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"


Constraints:

-107 <= num <= 107

"""
from itertools import chain


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = ''
        if num < 0:
            sign = '-'
            num = - num
        s = '0123456'
        ans = []
        while num:
            num, rem = divmod(num, 7)
            ans.append(s[rem])
        return ''.join(chain(sign, ans[::-1]))


def main():
    num = 100
    print(Solution().convertToBase7(num))


if __name__ == '__main__':
    main()

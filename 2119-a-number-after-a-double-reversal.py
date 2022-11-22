"""
Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2.
Return true if reversed2 equals num. Otherwise return false.



Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.


Constraints:

0 <= num <= 10^6
"""
from math import sqrt


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(s: str) -> str:
            ans = []
            leading = True
            for c in reversed(s):
                if c == '0' and leading:
                    continue
                leading = False
                ans.append(c)
            return ''.join(ans)

        if num == 0:
            return True
        s = str(num)
        return s == reverse(reverse(s))


def main():
    num = 526
    print(Solution().isSameAfterReversals(num))


if __name__ == '__main__':
    main()

"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constraints:

1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""
import itertools


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num:
            while stack and k and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)
        while k:
            stack.pop()
            k -= 1
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'


def main():
    print(Solution().removeKdigits("1000234536321", 2))
    # print(Solution().removeKdigits("112", 1))


if __name__ == '__main__':
    main()

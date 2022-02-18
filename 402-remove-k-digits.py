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
        digits = list(num)
        n = len(digits)
        if k >= n:
            return '0'

        ans = [digits[0]]
        i = 1
        while i < n:
            if digits[i] < ans[-1]:
                while ans and k > 0 and digits[i] < ans[-1]:
                    if ans.pop() != '0':
                        k -= 1
                        if k == 0:
                            break
            ans.append(digits[i])
            i += 1
        if k == 0:
            ans.extend(digits[i + 1:])
        if i == n:
            while k > 0:
                ans.pop()
                k -= 1
        s = ''.join(itertools.dropwhile(lambda digit: digit == '0', ans))
        return s if s else '0'


def main():
    print(Solution().removeKdigits("1000234536321", 2))
    # print(Solution().removeKdigits("112", 1))


if __name__ == '__main__':
    main()

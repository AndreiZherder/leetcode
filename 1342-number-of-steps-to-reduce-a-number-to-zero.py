"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.



Example 1:

Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation:
Step 1) 8 is even; divide by 2 and obtain 4.
Step 2) 4 is even; divide by 2 and obtain 2.
Step 3) 2 is even; divide by 2 and obtain 1.
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12


Constraints:

0 <= num <= 10^6
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        leading_zeroes_cnt = 0
        mask = 0x80000
        while not mask & num:
            leading_zeroes_cnt += 1
            mask >>= 1
        ones_cnt = 0
        while num:
            num &= num - 1
            ones_cnt += 1
        zeroes_cnt = 20 - leading_zeroes_cnt - ones_cnt
        return zeroes_cnt + ones_cnt * 2 - 1


def main():
    num = 123
    print(Solution().numberOfSteps(num))


if __name__ == '__main__':
    main()
"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.



Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021


Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 10^4
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = []
        while k:
            num1.append(k % 10)
            k //= 10
        num.reverse()
        carry = 0
        for i in range (min(len(num), len(num1))):
            carry, num[i] = divmod(num[i] + num1[i] + carry, 10)
        i += 1
        for i in range(min(len(num), len(num1)), max(len(num), len(num1))):
            if i < len(num1):
                if i < len(num):
                    carry, num[i] = divmod(num[i] + num1[i] + carry, 10)
                else:
                    carry, mod = divmod(num1[i] + carry, 10)
                    num.append(mod)
            else:
                if i < len(num):
                    carry, num[i] = divmod(num[i] + carry, 10)
                else:
                    carry, mod = divmod(carry, 10)
                    num.append(mod)
        if carry:
            num.append(carry)
        return num[::-1]



def main():
    num = [2,1,5]
    k = 806
    print(Solution().addToArrayForm(num, k))


if __name__ == '__main__':
    main()

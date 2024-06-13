"""
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers,
each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation:
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation:
The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199


Constraints:

1 <= num.length <= 35
num consists only of digits.


Follow up: How would you handle overflow for very large input integers?

"""
from functools import lru_cache


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        @lru_cache(None)
        def dp(i: int, previ1: int, previ2) -> bool:
            if i == n:
                return True
            ans = False
            prev1 = int(num[previ1:previ2])
            prev2 = int(num[previ2:i])
            for j in range(i, n):
                if int(num[i:j + 1]) == prev1 + prev2:
                    if j == i or num[i] != '0':
                        ans |= dp(j + 1, previ2, i)
            return ans
        n = len(num)
        if n < 3:
            return False
        ans = False
        if num[0] == '0':
            return dp(2, 0, 1)
        for previ2 in range(1, n - 1):
            if num[previ2] != '0':
                for i in range(previ2 + 1, n):
                    ans |= dp(i, 0, previ2)
            else:
                ans |= dp(previ2 + 1, 0, previ2)
        return ans



def main():
    num = '0235813'
    print(Solution().isAdditiveNumber(num))


if __name__ == '__main__':
    main()

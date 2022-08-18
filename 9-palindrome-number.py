"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = []
        while x:
            nums.append(x % 10)
            x //= 10
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True


def main():
    print(Solution().isPalindrome(1221))


if __name__ == '__main__':
    main()

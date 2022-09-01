"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
"""



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            if num <= mid * mid:
                right = mid - 1
            else:
                left = mid + 1
        return left * left == num


def main():
    num = 16
    print(Solution().isPerfectSquare(num))


if __name__ == '__main__':
    main()

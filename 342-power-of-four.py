"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.



Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true


Constraints:

-2^31 <= n <= 2^31 - 1


Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0 and n & 0xAAAAAAAA == 0


def main():
    n = 16
    print(Solution().isPowerOfFour(n))


if __name__ == '__main__':
    main()

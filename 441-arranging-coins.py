"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.



Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.


Constraints:

1 <= n <= 231 - 1

"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        def sn(a1: int, an: int, n: int) -> int:
            return (a1 + an) * n // 2

        def bsr(left: int, right: int) -> int:
            """
            TTTTFFFF
                |
            """

            def check(mid: int) -> bool:
                return sn(1, mid, mid) <= n

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        return bsr(0, n) - 1


def main():
    n = 8
    print(Solution().arrangeCoins(n))


if __name__ == '__main__':
    main()

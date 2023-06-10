"""
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed)
that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.



Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3


Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sn(a1: int, d: int, m: int) -> int:
            return (2 * a1 + d * (m - 1)) * m // 2

        def side_sum(x: int, m: int) -> int:
            if x - 1 >= m:
                return sn(x - 1, -1, m)
            else:
                return sn(x - 1, -1, x - 1) + m - (x - 1)

        left, right = 1, 10 ** 9
        while left <= right:
            mid = left + (right - left) // 2
            left_sum = side_sum(mid, index)
            right_sum = side_sum(mid, n - index - 1)
            if left_sum + mid + right_sum <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


def main():
    n = 10
    index = 4
    maxSum = 12
    print(Solution().maxValue(n, index, maxSum))


if __name__ == '__main__':
    main()

"""
Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


Follow up: If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""
from typing import List


def guess(num: int) -> int:
    if num == 6:
        return 0
    if num > 6:
        return -1
    else:
        return 1


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('Inf')
        a = 0
        for num in nums:
            a += num
            ans = max(ans, a)
            a = max(a, 0)
        return ans


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))


if __name__ == '__main__':
    main()

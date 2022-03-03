"""
An integer array is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        diff = nums[1] - nums[0]
        first = 0
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] != diff:
                length = i - first
                if length > 2:
                    ans += (1 + length - 2) * (length - 2) // 2
                diff = nums[i] - nums[i - 1]
                first = i - 1
        length = n - first
        if length > 2:
            ans += (1 + length - 2) * (length - 2) // 2
        return ans


def main():
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5, 6, 8, 8, 8, 8, 1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()

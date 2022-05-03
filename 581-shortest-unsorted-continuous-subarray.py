"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray
in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5


Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 1
        right = 0
        maximum = nums[0]
        minimum = nums[-1]
        for i, num in enumerate(nums):
            maximum = max(maximum, num)
            if num < maximum:
                right = i
        for i, num in enumerate(reversed(nums)):
            minimum = min(minimum, num)
            if num > minimum:
                left = len(nums) - i - 1
        return right - left + 1


def main():
    nums = [1, 2, 3, 2, 4, 5, 6, 5, 7]
    print(Solution().findUnsortedSubarray(nums))


if __name__ == '__main__':
    main()

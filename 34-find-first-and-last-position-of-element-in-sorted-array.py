"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def bisect_right(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        left = bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            left = -1
        right = bisect_right(nums, target) - 1
        if right == -1 or nums[right] != target:
            right = -1
        return [left, right]


def main():
    nums = []
    target = 10
    print(Solution().searchRange(nums, target))


if __name__ == '__main__':
    main()

"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""
from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_k(nums: List[int], left: int, right: int) -> int:
            if left > right:
                return left
            mid = left + (right - left) // 2
            if nums[left] > nums[mid]:
                return find_k(nums, left, mid)
            if nums[mid] > nums[right]:
                return find_k(nums, mid + 1, right)
            return left

        n = len(nums)
        k = find_k(nums, 0, len(nums) - 1)
        if k == 0:
            i = bisect_left(nums, target)
        elif nums[k] <= target <= nums[-1]:
            i = bisect_left(nums, target, lo=k, hi=n - 1)
        else:
            i = bisect_left(nums, target, lo=0, hi=k - 1)
        if i < n and nums[i] == target:
            return i
        else:
            return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))


if __name__ == '__main__':
    main()

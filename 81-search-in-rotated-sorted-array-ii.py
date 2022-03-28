"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates.
Would this affect the runtime complexity? How and why?
"""
from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False

    def pivot(self, nums: List[int], l: int, r: int) -> int:
        while nums[l] >= nums[r] and r - l > 1:
            m = (l + r) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[l] < nums[m]:
                l = m
            else:
                pivot = self.pivot(nums, l, m)
                if pivot != -1:
                    return pivot
                else:
                    pivot = self.pivot(nums, m, r)
                    return pivot
        if nums[l] == nums[r]:
            return -1
        else:
            return r

    def search(self, nums: List[int], target: int) -> bool:
        if nums[0] == target:
            return True
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return self.binary_search(nums, target)
        pivot = self.pivot(nums, l, r)
        if target >= nums[0]:
            return self.binary_search(nums[:pivot], target)
        else:
            return self.binary_search(nums[pivot:], target)


def main():
    nums = [1, 3]
    print(Solution().search(nums, 3))


if __name__ == '__main__':
    main()

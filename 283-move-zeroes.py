"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1


Follow up: Could you minimize the total number of operations done?
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


def main():
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))
    print(nums)


if __name__ == '__main__':
    main()

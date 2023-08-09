"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.


Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates.
Would this affect the runtime complexity? How and why?

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        FFFFTTTT
            |
        """
        def check(mid: int) -> bool:
            return nums[mid] < nums[0]

        n = len(nums)
        left = 0
        while left + 1 < n and nums[left + 1] == nums[0]:
            left += 1
        right = n - 1
        while right - 1 >= 0 and nums[right - 1] == nums[-1]:
            right -= 1
        r = right
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[0]:
                return min(nums)
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return nums[left] if left <= r else nums[0]


def main():
    nums = [2, 2, 2, 0, 1]
    print(Solution().findMin(nums))


if __name__ == '__main__':
    main()

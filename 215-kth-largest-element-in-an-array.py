"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
"""
from random import randrange
from typing import List, Tuple


class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> Tuple[int, int]:
        pos = randrange(left, right + 1)
        nums[left], nums[pos] = nums[pos], nums[left]
        j1, j2 = left, left
        for i in range(left + 1, right + 1):
            if nums[i] <= nums[left]:
                j2 += 1
                nums[i], nums[j2] = nums[j2], nums[i]
        for i in range(left + 1, j2 + 1):
            if nums[i] < nums[left]:
                j1 += 1
                nums[i], nums[j1] = nums[j1], nums[i]
        nums[left], nums[j1] = nums[j1], nums[left]
        return j1, j2

    def quick_select(self, nums: List[int], k: int, left: int, right: int):
        if left >= right:
            return nums[left]
        m1, m2 = self.partition(nums, left, right)
        if left <= k <= m1 - 1:
            return self.quick_select(nums, k, left, m1)
        elif m1 <= k <= m2:
            return nums[m1]
        else:
            return self.quick_select(nums, k, m2 + 1, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, len(nums) - k, 0, len(nums) - 1)


def main():
    nums = [7, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().findKthLargest(nums, k))


if __name__ == '__main__':
    main()

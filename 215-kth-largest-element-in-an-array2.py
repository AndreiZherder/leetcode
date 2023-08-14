"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from heapq import heapify, heapreplace
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = nums[:k]
        heapify(h)
        for i in range(k, n):
            if nums[i] > h[0]:
                heapreplace(h, nums[i])
        return h[0]


def main():
    nums = [7, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().findKthLargest(nums, k))


if __name__ == '__main__':
    main()

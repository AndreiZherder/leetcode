"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.


Constraints:

2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        prevmin = -1
        prevmax = -1
        prevborder = -1
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                prevborder = i
            if nums[i] == minK:
                prevmin = i
            if nums[i] == maxK:
                prevmax = i
            if prevmin != -1 and prevmax != -1:
                start = min(prevmin, prevmax)
                if prevborder < start:
                    ans += start - prevborder
        return ans


def main():
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    print(Solution().countSubarrays(nums, minK, maxK))


if __name__ == '__main__':
    main()

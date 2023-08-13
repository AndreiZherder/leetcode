"""
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is,
the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.



Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.


Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 106
"""
from functools import lru_cache
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(i: int) -> bool:
            if i >= n - 1:
                return False
            if i == n - 2:
                return nums[n - 2] == nums[n - 1]
            if i == n - 3:
                return (nums[n - 3] == nums[n - 2] == nums[n - 1]) or (
                            nums[n - 3] + 1 == nums[n - 2] and nums[n - 2] + 1 == nums[n - 1])
            ans1 = nums[i] == nums[i + 1] and dp(i + 2)
            ans2 = nums[i] == nums[i + 1] == nums[i + 2] and dp(i + 3)
            ans3 = nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2] and dp(i + 3)
            return ans1 or ans2 or ans3

        n = len(nums)
        return dp(0)


def main():
    nums = [4, 4, 4, 5, 6]
    print(Solution().validPartition(nums))


if __name__ == '__main__':
    main()

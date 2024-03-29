"""
You are given a binary array nums.

A subarray of an array is good if it contains exactly one element with the value 1.

Return an integer denoting the number of ways to split the array nums into good subarrays.
As the number may be too large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [0,1,0,0,1]
Output: 3
Explanation: There are 3 ways to split nums into good subarrays:
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]
Example 2:

Input: nums = [0,1,0]
Output: 1
Explanation: There is 1 way to split nums into good subarrays:
- [0,1,0]


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 1

"""
from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        one_exist = False
        cnt = 0
        ans = 1
        for num in nums:
            if not one_exist and num == 1:
                one_exist = True
            if one_exist and num == 0:
                cnt += 1
            if one_exist and num == 1:
                ans = (ans * (cnt + 1)) % mod
                cnt = 0
        if not one_exist:
            return 0
        return ans


def main():
    nums = [0, 1, 0, 0, 1]
    print(Solution().numberOfGoodSubarraySplits(nums))


if __name__ == '__main__':
    main()

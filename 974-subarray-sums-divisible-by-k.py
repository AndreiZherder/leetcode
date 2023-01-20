"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0


Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
2 <= k <= 10^4
"""
from collections import Counter
from itertools import accumulate
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = Counter({0: 1})
        ans = 0
        for num in accumulate(nums):
            ans += d[num % k]
            d[num % k] += 1
        return ans


def main():
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(Solution().subarraysDivByK(nums, k))


if __name__ == '__main__':
    main()
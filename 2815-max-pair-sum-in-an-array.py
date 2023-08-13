"""
You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers
from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.



Example 1:

Input: nums = [51,71,17,24,42]
Output: 88
Explanation:
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88.
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: No pair exists in nums with equal maximum digits.


Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        best = -1
        for i in range(n):
            for j in range(i + 1, n):
                if max(str(nums[i])) == max(str(nums[j])):
                    best = max(best, nums[i] + nums[j])
        return best


def main():
    nums = [51, 71, 17, 24, 42]
    print(Solution().maxSum(nums))


if __name__ == '__main__':
    main()

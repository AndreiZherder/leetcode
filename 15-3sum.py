"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        doubles = set()
        singles = set()
        zero_count = 0
        for num in nums:
            if num not in singles:
                singles.add(num)
            else:
                doubles.add(num)
            zero_count += 1 if num == 0 else 0
        if zero_count > 2:
            ans.append([0, 0, 0])
        for num in doubles:
            if -(num + num) in singles and num != 0:
                ans.append([num, num, -(num + num)])
        l = list(singles)
        for i in range(len(l)):
            hiden = set()
            for j in range(i + 1, len(l)):
                if -(l[i] + l[j]) in singles:
                    if -(l[i] + l[j]) != l[i] and -(l[i] + l[j]) != l[j]:
                        ans.append([l[i], l[j], -(l[i] + l[j])])
                        hiden.add(l[j])
                        singles.remove(l[j])
            singles |= hiden
            singles.remove(l[i])
        return ans


nums = [0, 0, 0]
solution = Solution()
print(solution.threeSum(nums))

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
        pairs = dict()
        singles = dict()
        for num in nums:
            if num not in pairs:
                if num not in singles:
                    singles[num] = 1
                else:
                    pairs[num] = 1
                    del singles[num]
        if pairs.get(0, 0) == 1 and not singles and len(nums) > 2:
            ans.append([0, 0, 0])
        for pair in pairs:
            if -(pair + pair) in singles:
                ans.append([pair, pair, -(pair + pair)])
        for k in pairs:
            singles[k] = 1
        l = sorted(list(singles))
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if -(l[i] + l[j]) in singles or -(l[i] + l[j]) in pairs:
                    if -(l[i] + l[j]) > l[j]:
                        ans.append([l[i], l[j], -(l[i] + l[j])])
        return ans

nums = [0, 0, 0]
solution = Solution()
print(solution.threeSum(nums))
'''
        triples = {tuple(sorted([nums[i], nums[j], nums[k]])) for k in range(n) for j in range(n) for i in range(n)
        if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0}
            ans = [list(triple) for triple in triples]
'''
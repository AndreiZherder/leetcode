"""
Given an array nums of n integers,
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twosum(nums: List[int], left: int, right: int, target: int) -> List[List[int]]:
            i, j = left, right
            ans = []
            while i < j:
                a = nums[i] + nums[j]
                if a > target:
                    j -= 1
                elif a < target:
                    i += 1
                else:
                    ans.append([nums[i], nums[j]])
                    while i < j and nums[i + 1] == nums[i]:
                        i += 1
                    i += 1
            return ans

        n = len(nums)
        ans = []
        nums.sort()

        j = n - 1
        for j in range(n - 1, 2, -1):
            if j < n - 1 and nums[j] == nums[j + 1]:
                continue
            for i in range(j - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                for a, b in twosum(nums, i + 1, j - 1, target - (nums[i] + nums[j])):
                    ans.append([nums[i], a, b, nums[j]])
        return ans


def main():
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    nums = [2, 2, 16, 2, 2, 2, -4, -6]
    target = 8
    print(Solution().fourSum(nums, target))


if __name__ == '__main__':
    main()

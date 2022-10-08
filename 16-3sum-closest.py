"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        d = abs(target - ans)
        for k in range(n - 2):
            i = k + 1
            j = n - 1
            while i < j:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < d:
                    d = abs(total - target)
                    ans = total
                if nums[i] + nums[j] < target - nums[k]:
                    i += 1
                else:
                    j -= 1
        return ans


def main():
    nums = [-1, 2, -4, -1]
    target = 1
    print(Solution().threeSumClosest(nums, target))


if __name__ == '__main__':
    main()

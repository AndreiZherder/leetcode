"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109


Follow up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len(nums) == 1:
            return [nums[0]]
        ans1 = -2
        ans2 = -1
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == ans1:
                cnt1 += 1
            elif num == ans2:
                cnt2 += 1
            elif cnt1 == 0:
                ans1 = num
                cnt1 = 1
            elif cnt2 == 0:
                ans2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ans = []
        if nums.count(ans1) > n // 3:
            ans.append(ans1)
        if nums.count(ans2) > n // 3:
            ans.append(ans2)

        return ans


def main():
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))


if __name__ == '__main__':
    main()

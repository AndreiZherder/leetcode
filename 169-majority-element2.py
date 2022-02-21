"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        majority_element = float('Inf')
        for num in nums:
            if num == majority_element:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                majority_element = num
                cnt = 1
        return majority_element


def main():
    nums = [3, 3, 4]
    print(Solution().majorityElement(nums))


if __name__ == '__main__':
    main()

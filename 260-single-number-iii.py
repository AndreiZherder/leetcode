"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear
exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]


Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.

"""
from functools import reduce
from operator import xor
from typing import List


def least_set_bit(n: int) -> int:
    """
    least_set_bit(12) -> 4
    1100 -> 0100
    """
    return n & -n


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = reduce(xor, nums)
        x = least_set_bit(total)
        ans1 = 0
        ans2 = 0
        for num in nums:
            if num & x:
                ans1 ^= num
            else:
                ans2 ^= num
        return [ans1, ans2]


def main():
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))


if __name__ == '__main__':
    main()

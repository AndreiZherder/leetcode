"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = [0 for i in range(32)]
        neg = 0
        for num in nums:
            if num < 0:
                neg += 1
                num = -num
            for j in range(32):
                if num & 1 << j:
                    cnt[j] += 1
        ans = 0
        for j in range(32):
            if cnt[j] % 3:
                ans |= 1 << j
        return ans if neg % 3 == 0 else -ans


def main():
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(Solution().singleNumber(nums))


if __name__ == '__main__':
    main()

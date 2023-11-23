"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
                k += 1
        cur = 1
        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                if nums[x - 1] > 0:
                    nums[x - 1] = -nums[x - 1]
                while cur <= n - k and nums[cur - 1] < 0:
                    cur += 1
        return cur


def main():
    nums = [3, 4, -1, 1]
    print(Solution().firstMissingPositive(nums))


if __name__ == '__main__':
    main()

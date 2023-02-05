"""
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is,
(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12


Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f = -10 ** 20
        s = -10 ** 20
        for num in nums:
            if num >= f:
                f, s = num, f
            elif num >= s:
                s = num
        return (f - 1) * (s - 1)


def main():
    nums = [3,4,5,2]
    print(Solution().maxProduct(nums))


if __name__ == '__main__':
    main()
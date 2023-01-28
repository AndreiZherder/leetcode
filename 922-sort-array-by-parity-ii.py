"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.



Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]


Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000


Follow Up: Could you solve it in-place?
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 1
        j = 2
        n = len(nums)
        for k in range(n):
            if k % 2 == 0:
                if nums[k] % 2 == 1:
                    while nums[i] % 2 == 1:
                        i += 2
                    nums[k], nums[i] = nums[i], nums[k]
                    i += 2
            else:
                if nums[k] % 2 == 0:
                    while nums[j] % 2 == 0:
                        j += 2
                    nums[k], nums[j] = nums[j], nums[k]
                    j += 2
        return nums


def main():
    nums = [4, 2, 5, 7]
    print(Solution().sortArrayByParityII(nums))


if __name__ == '__main__':
    main()

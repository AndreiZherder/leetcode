"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:

n == nums.length
1 <= n <= 2 * 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        prev = nums[-1]
        stack = [nums[-1]]
        second = None
        for num in reversed(nums):
            if second is not None and num < second:
                return True
            if num < prev:
                stack.append(num)
            if num > prev:
                if not stack:
                    second = prev
                else:
                    while stack and stack[-1] < num:
                        second = stack.pop()
            prev = num
        return False


def main():
    nums = [2, 4, 3, 1]
    # nums = [-1, 3, 2, 0]
    # nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    # nums = [3, 5, 0, 3, 4]
    print(Solution().find132pattern(nums))


if __name__ == '__main__':
    main()

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        best = 10 ** 20
        i = 0
        j = 0
        total = 0
        while i < n:
            total += nums[i]
            while total >= target:
                best = min(best, i - j + 1)
                total -= nums[j]
                j += 1
            i += 1
        return best if best != 10 ** 20 else 0


def main():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(target, nums))


if __name__ == '__main__':
    main()

"""
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k
with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.



Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)

"""
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        total1 = 0
        total2 = 0
        total3 = 0
        mx1 = 0
        mx12 = 0
        maxi1 = 0
        maxi12 = []
        mx = 0
        ans = []
        for i in range(k * 2, len(nums)):
            total1 += nums[i - k * 2]
            total2 += nums[i - k]
            total3 += nums[i]
            if i >= k * 3 - 1:
                if total1 > mx1:
                    mx1 = total1
                    maxi1 = i - k * 3 + 1
                if mx1 + total2 > mx12:
                    mx12 = mx1 + total2
                    maxi12 = [maxi1, i - k * 2 + 1]
                if mx12 + total3 > mx:
                    mx = mx12 + total3
                    ans = [maxi12[0], maxi12[1], i - k + 1]
                total1 -= nums[i - k * 3 + 1]
                total2 -= nums[i - k * 2 + 1]
                total3 -= nums[i - k + 1]
        return ans


def main():
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    print(Solution().maxSumOfThreeSubarrays(nums, k))


if __name__ == '__main__':
    main()

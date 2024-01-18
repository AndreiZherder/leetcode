"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in
the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length

"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = 0
        flipped = 0
        j = 0
        for i in range(n):
            if nums[i] == 0:
                if flipped < k:
                    flipped += 1
                else:
                    while nums[j] == 1:
                        j += 1
                    j += 1
            best = max(best, i - j + 1)
        return best


def main():
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(Solution().longestOnes(nums, k))


if __name__ == '__main__':
    main()

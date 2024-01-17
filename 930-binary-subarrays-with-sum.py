"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15


Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length

"""
from collections import Counter
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = Counter()
        d[0] = 1
        pref = 0
        ans = 0
        for num in nums:
            pref += num
            ans += d[pref - goal]
            d[pref] += 1
        return ans


def main():
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(Solution().numSubarraysWithSum(nums, goal))


if __name__ == '__main__':
    main()

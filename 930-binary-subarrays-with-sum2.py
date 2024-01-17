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
        def f(goal: int) -> int:
            if goal < 0:
                return 0
            n = len(nums)
            j = 0
            ans = 0
            total = 0
            for i in range(n):
                total += nums[i]
                if total <= goal:
                    ans += i - j + 1
                else:
                    while total > goal:
                        total -= nums[j]
                        j += 1
                    ans += i - j + 1
            return ans

        return f(goal) - f(goal - 1)


def main():
    nums = [0, 0, 0, 0, 0]
    goal = 0
    print(Solution().numSubarraysWithSum(nums, goal))


if __name__ == '__main__':
    main()

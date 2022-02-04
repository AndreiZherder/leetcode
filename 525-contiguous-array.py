"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        d[0] = -1
        ans = 0
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
            if count in d:
                ans = max(ans, i - d[count])
            else:
                d[count] = i
        return ans


def main():
    print(Solution().findMaxLength([0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]))


if __name__ == '__main__':
    main()

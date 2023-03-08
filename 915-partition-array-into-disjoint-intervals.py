"""
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.



Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Constraints:

2 <= nums.length <= 10^5
0 <= nums[i] <= 10^6
There is at least one valid answer for the given input.
"""
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [10 ** 20 for i in range(n)]
        pref[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            pref[i] = min(pref[i + 1], nums[i])
        ans = 0
        mx = -10 ** 20
        for i in range(n - 1):
            mx = max(mx, nums[i])
            if mx <= pref[i + 1]:
                return i + 1


def main():
    nums = [5, 0, 3, 8, 6]
    print(Solution().partitionDisjoint(nums))


if __name__ == '__main__':
    main()

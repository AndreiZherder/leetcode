"""
Given an integer array nums and an integer k, return the length of the shortest non-empty
subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3


Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109

"""
from itertools import accumulate
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        def bsr(left: int, right: int) -> int:
            """
            TTTTFFFF
                |
            """

            def check(mid: int) -> bool:
                return pref[i] + k <= pref[stack[mid]]

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        n = len(nums)
        if any(num >= k for num in nums):
            return 1
        pref = list(accumulate(nums, initial=0))
        n += 1
        stack = []
        best = 10 ** 20
        for i in range(n - 1, -1, -1):
            while stack and pref[stack[-1]] <= pref[i]:
                stack.pop()
            stack.append(i)
            index = bsr(0, len(stack) - 1) - 1
            if index >= 0:
                j = stack[index]
                best = min(best, j - i)
        return best if best != 10 ** 20 else -1


def main():
    nums = [84, -37, 32, 40, 95]
    k = 167
    print(Solution().shortestSubarray(nums, k))


if __name__ == '__main__':
    main()

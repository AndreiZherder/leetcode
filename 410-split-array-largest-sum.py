"""
Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
"""
import itertools
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if m == n:
            return max(nums)
        if m == 1:
            return sum(nums)
        acc = list(itertools.accumulate(nums))
        left = acc[0]
        right = acc[-1]
        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            parts = self.count_parts(acc, m, mid)
            if parts == m:
                if mid <= ans:
                    ans = mid
                    right = mid - 1
                else:
                    return ans
            elif parts < m:
                if mid <= ans:
                    ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def count_parts(self, acc: List[int], m: int, sum: int) -> int:
        n = len(acc)
        left = 0
        right = len(acc) - 1
        parts = 1
        x = 0
        while parts <= m:
            while left <= right:
                mid = (left + right) // 2
                if acc[mid] - x <= sum:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == n:
                return parts
            else:
                parts += 1
                x = acc[left - 1]
                right = len(acc) - 1
        return parts


def main():
    nums = [2, 3, 1, 1, 1, 1, 1]
    m = 5
    print(Solution().splitArray(nums, m))


if __name__ == '__main__':
    main()

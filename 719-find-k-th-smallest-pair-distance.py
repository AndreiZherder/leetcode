"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j]
where 0 <= i < j < nums.length.



Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5


Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2

"""
from bisect import bisect_right
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def bsl(left: int, right: int) -> int:
            """
            FFFFTTTT
                |
            """

            def check(mid: int) -> bool:
                cnt = 0
                for i, num in enumerate(nums):
                    j = bisect_right(nums, num + mid)
                    cnt += j - i - 1
                return cnt >= k

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        nums.sort()
        return bsl(0, nums[-1] - nums[0])


def main():
    nums = [1, 3, 1]
    k = 1
    print(Solution().smallestDistancePair(nums, k))


if __name__ == '__main__':
    main()

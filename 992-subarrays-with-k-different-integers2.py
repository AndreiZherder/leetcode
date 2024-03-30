"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length

"""
from collections import Counter
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def solve(nums: List[int], k: int) -> int:
            n = len(nums)
            c = Counter()
            j = 0
            ans = 0
            for i in range(n):
                c[nums[i]] += 1
                while len(c) > k:
                    c[nums[j]] -= 1
                    if c[nums[j]] == 0:
                        del c[nums[j]]
                    j += 1
                ans += i - j + 1
            return ans
        return solve(nums, k) - solve(nums, k - 1)


def main():
    nums = [1, 1, 1]
    k = 1
    print(Solution().subarraysWithKDistinct(nums, k))


if __name__ == '__main__':
    main()

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
        n = len(nums)
        i = n - 1
        left = n - 1
        right = n - 1
        ans = 0
        d = Counter()
        d1 = Counter()
        for i in range(n - 1, k - 2, -1):
            while len(d) <= k and left >= 0:
                if len(d) == k and nums[left] not in d:
                    break
                else:
                    d[nums[left]] += 1
                    left -= 1

            while len(d1) < k and right >= 0:
                d1[nums[right]] += 1
                right -= 1

            if len(d) >= k:
                if k == 1:
                    ans += right - left
                else:
                    ans += right + 1 - left
            d[nums[i]] -= 1
            if d[nums[i]] == 0:
                del d[nums[i]]
            d1[nums[i]] -= 1
            if d1[nums[i]] == 0:
                del d1[nums[i]]
        if k == 1:
            ans += n
        return ans


def main():
    nums = [1, 1, 1]
    k = 1
    print(Solution().subarraysWithKDistinct(nums, k))


if __name__ == '__main__':
    main()

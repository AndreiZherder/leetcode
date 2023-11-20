"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.


Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109
"""
from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        total = 0
        counter = Counter()
        ans = 0
        while i < n or total >= k:
            if total < k:
                total += counter[nums[i]]
                counter[nums[i]] += 1
                i += 1
                if total >= k:
                    ans += n - i + 1
            else:
                counter[nums[j]] -= 1
                total -= counter[nums[j]]
                j += 1
                if total >= k:
                    ans += n - i + 1
        return ans


def main():
    nums = [3, 1, 4, 3, 2, 2, 4]
    k = 2
    print(Solution().countGood(nums, k))


if __name__ == '__main__':
    main()

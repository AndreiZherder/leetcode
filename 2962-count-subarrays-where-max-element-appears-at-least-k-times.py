"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are:
[1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105

"""
from typing import List


# https://www.geeksforgeeks.org/number-subarrays-sum-less-k/
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        nums = [1 if num == mx else 0 for num in nums]
        n = len(nums)
        start = 0
        end = 0
        count = 0
        total = nums[0]

        while start < n and end < n:
            if total < k:
                end += 1
                if end >= start:
                    count += end - start
                if end < n:
                    total += nums[end]
            else:
                total -= nums[start]
                start += 1
        return n * (n + 1) // 2 - count


def main():
    nums = [0, 1, 0, 1, 1]
    k = 2
    print(Solution().countSubarrays(nums, k))


if __name__ == '__main__':
    main()

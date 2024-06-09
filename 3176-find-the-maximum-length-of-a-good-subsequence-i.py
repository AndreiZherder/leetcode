"""
You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good
if there are at most k indices i in the range [0, seq.length - 2] such that seq[i] != seq[i + 1].

Return the maximum possible length of a good
subsequence
 of nums.



Example 1:

Input: nums = [1,2,1,1,3], k = 2

Output: 4

Explanation:

The maximum length subsequence is [1,2,1,1,3].

Example 2:

Input: nums = [1,2,3,4,5,1], k = 0

Output: 2

Explanation:

The maximum length subsequence is [1,2,3,4,5,1].



Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 109
0 <= k <= min(nums.length, 25)

"""
from functools import lru_cache
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k: int):
            if i == n:
                return 0
            ans = 0
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    ans = max(ans, 1 + dp(j, k))
                else:
                    if k > 0:
                        ans = max(ans, 1 + dp(j, k - 1))
            return ans
        n = len(nums)
        return max(dp(i, k) for i in range(n)) + 1


def main():
    nums = [1,2,1,1,3]
    k = 2
    print(Solution().maximumLength(nums, k))


if __name__ == '__main__':
    main()

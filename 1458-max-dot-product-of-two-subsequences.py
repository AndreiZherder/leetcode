"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).



Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.


Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i == n or j == m:
                return 0
            return max(nums1[i] * nums2[j] + dp(i + 1, j + 1), dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1))

        n = len(nums1)
        m = len(nums2)
        if nums2[0] < 0:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        if nums1[0] < 0 and nums2[0] > 0:
            if all(num < 0 for num in nums1) and all(num > 0 for num in nums2):
                return max(nums1) * min(nums2)
        return dp(0, 0)


def main():
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]
    print(Solution().maxDotProduct(nums1, nums2))


if __name__ == '__main__':
    main()

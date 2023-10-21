"""
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array
such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j,
the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array,
leaving the remaining elements in their original order.



Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [nums[i] for i in range(n)]
        dp.append(0)
        q = deque([-1])
        for i in range(n):
            while q[0] < i - k:
                q.popleft()
            dp[i] = max(dp[i], dp[q[0]] + nums[i])
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        return max(dp[:n])


def main():
    nums = [10, 2, -10, 5, 20]
    k = 2
    print(Solution().constrainedSubsetSum(nums, k))


if __name__ == '__main__':
    main()

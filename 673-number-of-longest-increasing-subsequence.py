"""
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.



Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1,
so output 5.


Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106

"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[] for i in range(n)]
        for i in range(n):
            dp[i] = [1, 1]
            stack = []
            for j in range(i):
                if nums[j] < nums[i]:
                    while stack and dp[stack[-1]][0] < dp[j][0]:
                        stack.pop()
                    if not stack or dp[j][0] == dp[stack[-1]][0]:
                        stack.append(j)
            if stack:
                dp[i][0] = dp[stack[-1]][0] + 1
                dp[i][1] = sum(dp[stack[k]][1] for k in range(len(stack)))
        mx = max(dp)[0]
        ans = sum(dp[i][1] for i in range(n) if dp[i][0] == mx)
        return ans


def main():
    nums = [1, 3, 5, 4, 7]
    print(Solution().findNumberOfLIS(nums))


if __name__ == '__main__':
    main()

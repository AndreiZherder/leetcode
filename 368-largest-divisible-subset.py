"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair
(answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

"""
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]
        prev = [-1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        maxi = 0
        for i in range(1, n):
            if dp[i] > dp[maxi]:
                maxi = i
        i = maxi
        ans = []
        while i != -1:
            ans.append(nums[i])
            i = prev[i]
        return ans[::-1]



def main():
    nums = [1, 2, 4, 8]
    print(Solution().largestDivisibleSubset(nums))


if __name__ == '__main__':
    main()

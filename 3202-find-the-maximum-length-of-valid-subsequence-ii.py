"""
You are given an integer array nums and a positive integer k.
A
subsequence
 sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.


Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].



Constraints:

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103
"""
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0 for j in range(k)] for i in range(n)]
        for i in range(n):
            for j in range(i):
                x = (nums[j] + nums[i]) % k
                dp[i][x] = max(dp[i][x], dp[j][x] + 1, 2)
        return max((max(row) for row in dp))


def main():
    nums = [1, 4, 2, 3, 1, 4]
    k = 3
    print(Solution().maximumLength(nums, k))


if __name__ == '__main__':
    main()

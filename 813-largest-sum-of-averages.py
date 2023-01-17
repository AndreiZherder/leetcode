"""
You are given an integer array nums and an integer k.
You can partition the array into at most k non-empty adjacent subarrays.
The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions.
Answers within 10-6 of the actual answer will be accepted.



Example 1:

Input: nums = [9,1,2,3,9], k = 3
Output: 20.00000
Explanation:
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
Example 2:

Input: nums = [1,2,3,4,5,6,7], k = 4
Output: 20.50000


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 104
1 <= k <= nums.length
"""
from functools import lru_cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @lru_cache(None)
        def dfs(i: int, k: int) -> float:
            if k == 1:
                return sum(nums[i:]) / (n - i)
            best = -10 ** 20
            total = 0
            for j in range(i, n - k + 1):
                total += nums[j]
                best = max(best, total / (j - i + 1) + dfs(j + 1, k - 1))
            return best

        n = len(nums)
        return dfs(0, k)


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 4
    print(Solution().largestSumOfAverages(nums, k))


if __name__ == '__main__':
    main()

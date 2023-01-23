"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k
non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 10^4
The frequency of each element is in the range [1, 4].
"""
from functools import lru_cache
from itertools import combinations
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        @lru_cache(None)
        def dfs(mask: int, k: int) -> bool:
            if k == 0:
                if mask & (2 ** n - 1) == 2 ** n - 1:
                    return True
                else:
                    return False
            bit = 1
            free_indexes = []
            for i in range(n):
                if mask & bit == 0:
                    free_indexes.append(i)
                bit <<= 1
            for i in range(1, n - k + 2):
                for comb in combinations(free_indexes, i):
                    total = 0
                    for j in comb:
                        total += nums[j]
                        if total > target:
                            break
                    else:
                        if total == target:
                            for j in comb:
                                mask |= 1 << j
                            if dfs(mask, k - 1):
                                return True
                            for j in comb:
                                mask &= ~(1 << j)
            return False

        target = sum(nums)
        if target % k != 0:
            return False
        target //= k
        n = len(nums)
        nums.sort(reverse=True)
        return dfs(0, k)


def main():
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(Solution().canPartitionKSubsets(nums, k))


if __name__ == '__main__':
    main()

"""
You are given a 0-indexed integer array nums containing n distinct positive integers.
A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.
Return the total number of special permutations. As the answer could be large, return it modulo 109 + 7.



Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.


Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 109

"""
from functools import lru_cache
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(prev: int, used: int) -> int:
            if used == 2 ** n - 1:
                return 1
            ans = 0
            for j in range(n):
                if 1 << j & masks[prev] and not used & 1 << j:
                    used |= 1 << j
                    ans = (ans + dp(j, used)) % mod
                    used &= ~(1 << j)
            return ans

        mod = 10 ** 9 + 7
        n = len(nums)
        masks = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if j != i and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    masks[i] |= 1 << j
        ans = 0
        for i in range(n):
            ans = (ans + dp(i, 1 << i)) % mod
        return ans


def main():
    nums = [2, 3, 6]
    print(Solution().specialPerm(nums))


if __name__ == '__main__':
    main()

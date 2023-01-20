"""
Given an integer array nums, return all the different possible non-decreasing subsequences
of the given array with at least two elements. You may return the answer in any order.



Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]


Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int) -> List[List[int]]:
            ans = []
            seen = set()
            for j in range(i + 1, n):
                if nums[j] >= nums[i] and nums[j] not in seen:
                    seen.add(nums[j])
                    ans.append([nums[j]])
                    for path in dfs(j):
                        ans.append([nums[j]] + path)
            return ans
        n = len(nums)
        ans = []
        seen = set()
        for i in range(n - 1):
            if nums[i] not in seen:
                seen.add(nums[i])
                for path in dfs(i):
                    ans.append([nums[i]] + path)
        return ans


def main():
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))


if __name__ == '__main__':
    main()

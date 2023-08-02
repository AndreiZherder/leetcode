"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(used: int, cur: List[int]):
            if used == (1 << n) - 1:
                ans.append(cur.copy())
                return
            for j in range(n):
                if used & (1 << j) == 0:
                    used |= 1 << j
                    cur.append(nums[j])
                    backtrack(used, cur)
                    cur.pop()
                    used &= ~(1 << j)

        n = len(nums)
        ans = []
        backtrack(0, [])
        return ans


def main():
    nums = [1, 2, 3]
    print(Solution().permute(nums))


if __name__ == '__main__':
    main()

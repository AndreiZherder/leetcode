"""
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(2 ** n):
            cur = []
            j = 0
            for j in range(n):
                if i & 1 << j:
                    cur.append(nums[j])
            ans.add(tuple(sorted(cur)))
        return [list(t) for t in ans]



def main():
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()

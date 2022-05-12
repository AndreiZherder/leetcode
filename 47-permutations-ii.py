"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from collections import deque
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(deque(nums))

    def dfs(self, queue: deque) -> List[List[int]]:
        ans = []
        seen = set()
        for i in range(len(queue)):
            num = queue.popleft()
            if num not in seen:
                seen.add(num)
                seqs = self.dfs(queue)
                if seqs:
                    for seq in seqs:
                        ans.append([num] + seq)
                else:
                    ans.append([num])
            queue.append(num)
        return ans


def main():
    nums = [1, 1, 2, 2]
    print(Solution().permuteUnique(nums))


if __name__ == '__main__':
    main()

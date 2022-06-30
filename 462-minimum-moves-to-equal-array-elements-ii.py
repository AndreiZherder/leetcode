"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16


Constraints:

n == nums.length
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from random import randrange
from typing import List, Tuple


class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> Tuple[int, int]:
        pos = randrange(left, right + 1)
        nums[left], nums[pos] = nums[pos], nums[left]
        j1, j2 = left, left
        for i in range(left + 1, right + 1):
            if nums[i] <= nums[left]:
                j2 += 1
                nums[i], nums[j2] = nums[j2], nums[i]
        for i in range(left + 1, j2 + 1):
            if nums[i] < nums[left]:
                j1 += 1
                nums[i], nums[j1] = nums[j1], nums[i]
        nums[left], nums[j1] = nums[j1], nums[left]
        return j1, j2

    def quick_select(self, nums: List[int], k: int, left: int, right: int):
        if left >= right:
            return nums[left]
        m1, m2 = self.partition(nums, left, right)
        if left <= k <= m1 - 1:
            return self.quick_select(nums, k, left, m1)
        elif m1 <= k <= m2:
            return nums[m1]
        else:
            return self.quick_select(nums, k, m2 + 1, right)

    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        m = self.quick_select(nums, n // 2, 0, n - 1)
        ans = 0
        for num in nums:
            ans += abs(num - m)
        return ans


def main():
    nums = [1, 1, 2, 1]
    print(Solution().quick_select(nums, len(nums) // 2, 0, len(nums) - 1))
    print(Solution().minMoves2(nums))


if __name__ == '__main__':
    main()

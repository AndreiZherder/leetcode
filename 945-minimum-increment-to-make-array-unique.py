"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length
and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

"""
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        s = set(nums)
        ans = 0
        prev = -1
        p = nums[0] + 1
        for num in nums:
            if num == prev:
                while p in s:
                    p += 1
                ans += p - num
                p += 1
            prev = num
            p = max(p, num + 1)
        return ans


def main():
    nums = [3, 2, 1, 2, 1, 7]
    print(Solution().minIncrementForUnique(nums))


if __name__ == '__main__':
    main()

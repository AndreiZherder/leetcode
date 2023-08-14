"""
Given an integer array nums, return the number of triplets chosen
from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

"""
from bisect import bisect_left
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                ans += max(0, bisect_left(nums, nums[i] + nums[j]) - 1 - j)
        return ans


def main():
    nums = [2, 2, 3, 4]
    print(Solution().triangleNumber(nums))


if __name__ == '__main__':
    main()

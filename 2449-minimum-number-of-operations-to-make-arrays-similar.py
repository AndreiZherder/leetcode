"""
You are given two positive integer arrays nums and target, of the same length.

In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:

set nums[i] = nums[i] + 2 and
set nums[j] = nums[j] - 2.
Two arrays are considered to be similar if the frequency of each element is the same.

Return the minimum number of operations required to make nums similar to target.
The test cases are generated such that nums can always be similar to target.



Example 1:

Input: nums = [8,12,6], target = [2,14,10]
Output: 2
Explanation: It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,5], target = [4,1,3]
Output: 1
Explanation: We can make nums similar to target in one operation:
- Choose i = 1 and j = 2, nums = [1,4,3].
Example 3:

Input: nums = [1,1,1,1,1], target = [1,1,1,1,1]
Output: 0
Explanation: The array nums is already similiar to target.


Constraints:

n == nums.length == target.length
1 <= n <= 105
1 <= nums[i], target[i] <= 106
It is possible to make nums similar to target.
"""
from typing import List

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        ans = 0
        nums1 = [num for num in nums if num % 2 == 0]
        nums2 = [num for num in nums if num % 2 == 1]
        target1 = [num for num in target if num % 2 == 0]
        target2 = [num for num in target if num % 2 == 1]
        for x, y in zip(sorted(nums1), sorted(target1)):
            ans += abs(x - y)
        for x, y in zip(sorted(nums2), sorted(target2)):
            ans += abs(x - y)
        return ans // 4


def main():
    nums = [1, 2, 5]
    target = [4, 1, 3]
    print(Solution().makeSimilar(nums, target))


if __name__ == '__main__':
    main()

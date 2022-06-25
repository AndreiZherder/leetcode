"""
Given an array nums with n integers,
your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

n == nums.length
1 <= n <= 10^4
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        modified = False
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                if i + 2 < n:
                    if nums[i + 2] >= nums[i]:
                        nums[i + 1] = nums[i]
                        if modified:
                            return False
                        else:
                            modified = True
                    elif i == 0:
                        nums[i] = nums[i + 1]
                        if modified:
                            return False
                        else:
                            modified = True
                    elif nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i - 1]
                        if modified:
                            return False
                        else:
                            modified = True
                    else:
                        return False
                else:
                    nums[i + 1] = nums[i]
                    if modified:
                        return False
                    else:
                        modified = True
        return True


def main():
    # nums = [4, 2, 3]
    # nums = [4, 2, 1]
    nums = [1, 2, 3, 4, 3, 3]
    print(Solution().checkPossibility(nums))


if __name__ == '__main__':
    main()

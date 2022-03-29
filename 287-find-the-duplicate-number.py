"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
https://stackoverflow.com/questions/2936213/how-does-finding-a-cycle-start-node-in-a-cycle-linked-list-work
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        met = 0
        while True:
            fast = nums[nums[fast]] if not met else nums[fast]
            slow = nums[slow]
            if fast == slow:
                if not met:
                    if slow == 0:
                        return nums[0]
                    slow = 0
                    met = 1
                else:
                    return slow


def main():
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))


if __name__ == '__main__':
    main()

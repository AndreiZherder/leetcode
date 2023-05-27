"""
You are given a 0-indexed integer array nums representing the score of students in an exam.
The teacher would like to form one non-empty group of students with maximal strength,
where the strength of a group of students of indices
i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik].

Return the maximum strength of a group the teacher can create.



Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5].
Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20.
We cannot achieve greater strength.


Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9
"""
from functools import reduce
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)

        if len(nums) == 0:
            return 0

        if len(nums) == 1 and nums[0] < 0:
            return 0

        m = sum(num < 0 for num in nums)
        if m % 2 == 0:
            return reduce(lambda x, y: x * y, nums)
        else:
            x = max(num for num in nums if num < 0)
            nums.remove(x)
            return reduce(lambda x, y: x * y, nums)


def main():
    nums = [3, -1, -5, 2, 5, -9]
    print(Solution().maxStrength(nums))


if __name__ == '__main__':
    main()

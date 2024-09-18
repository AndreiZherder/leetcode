"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted((str(num) for num in nums), key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))).lstrip('0') or '0'


def main():
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))


if __name__ == '__main__':
    main()

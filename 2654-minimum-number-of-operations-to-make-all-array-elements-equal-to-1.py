"""
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation
on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.



Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.


Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106
"""
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = nums.count(1)
        if cnt:
            return n - cnt
        g = reduce(gcd, nums)
        if g != 1:
            return -1
        best = n
        for i in range(n):
            cur = nums[i]
            for j in range(i + 1, n):
                if gcd(cur, nums[j]) == 1:
                    best = min(best, j - i - 1)
                    break
                cur = gcd(cur, nums[j])
        return n + best


def main():
    nums = [2, 6, 3, 4]
    print(Solution().minOperations(nums))


if __name__ == '__main__':
    main()

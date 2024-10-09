"""
AYou are given an array of integers nums of size 3.

Return the maximum possible number whose binary representation can be formed by concatenating the binary
representation of all elements in nums in some order.

Note that the binary representation of any number does not contain leading zeros.



Example 1:

Input: nums = [1,2,3]

Output: 30

Explanation:

Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.

Example 2:

Input: nums = [2,8,16]

Output: 1296

Explanation:

Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000", which is the binary representation
of 1296.



Constraints:

nums.length == 3
1 <= nums[i] <= 127

"""
from itertools import permutations
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def f(nums) -> int:
            return int(''.join(bin(num)[2:] for num in nums), 2)
        return max(f(perm) for perm in permutations(nums))


def main():
    nums = [2, 8, 16]
    print(Solution().maxGoodNumber(nums))


if __name__ == '__main__':
    main()

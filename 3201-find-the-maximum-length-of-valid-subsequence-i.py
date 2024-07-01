"""
You are given an integer array nums.
A
subsequence
 sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.



Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].



Constraints:

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107
"""
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        alternate = 0
        prev = nums[0] % 2
        for num in nums[1:]:
            if (num % 2) ^ (prev % 2):
                alternate += 1
            prev = num

        odd = 0
        even = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        return max(2, alternate + 1, odd, even)


def main():
    nums = [1, 2, 1, 1, 2, 1, 2]
    print(Solution().maximumLength(nums))


if __name__ == '__main__':
    main()

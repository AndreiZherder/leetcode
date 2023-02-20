"""
You are given a 0-indexed integer array nums.

We say that an integer x is expressible from nums if there exist some integers
0 <= index1 < index2 < ... < indexk < nums.length for which nums[index1] | nums[index2] | ... | nums[indexk] = x.
In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums.

Return the minimum positive non-zero integer that is not expressible from nums.



Example 1:

Input: nums = [2,1]
Output: 4
Explanation: 1 and 2 are already present in the array. We know that 3 is expressible,
since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
Example 2:

Input: nums = [5,3,2]
Output: 1
Explanation: We can show that 1 is the smallest number that is not expressible.


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
from bisect import bisect_left
from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        while i < 32:
            ans = 1 << i
            j = bisect_left(nums, ans)
            if j == n or ans != nums[j]:
                return ans
            i += 1
        return -1


def main():
    nums = [5, 3, 2]
    print(Solution().minImpossibleOR(nums))


if __name__ == '__main__':
    main()
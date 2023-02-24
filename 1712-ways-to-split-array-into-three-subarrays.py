"""
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.


Constraints:

3 <= nums.length <= 10^5
0 <= nums[i] <= 10^4
"""
from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        prefix = list(accumulate(nums))
        n = len(nums)
        x = 0
        ans = 0
        for i in range(n - 2):
            x += nums[i]
            j = bisect_left(prefix, 2 * x)
            k = bisect_right(prefix, x + (prefix[-1] - x) // 2) - 1
            j = max(i + 1, j)
            k = min(k, n - 2)
            if k >= j:
                ans = (ans + (k - j + 1)) % mod
        return ans


def main():
    nums = [1, 2, 2, 2, 5, 0]
    print(Solution().waysToSplit(nums))


if __name__ == '__main__':
    main()

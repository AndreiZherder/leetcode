"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums
and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.



Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""
from itertools import accumulate
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def bsr(left: int, right: int) -> int:
            """
            TTTTFFFF
                |
            """
            def check(mid: int) -> bool:
                return pref[mid + 1] - pref[i] + k >= (mid - i + 1) * nums[i]

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        n = len(nums)
        nums.sort(reverse=True)
        pref = list(accumulate(nums, initial=0))
        best = 1
        for i in range(n):
            j = bsr(i, n - 1) - 1
            best = max(best, j - i + 1)
        return best


def main():
    nums = [1, 4, 8, 13]
    k = 5
    print(Solution().maxFrequency(nums, k))


if __name__ == '__main__':
    main()

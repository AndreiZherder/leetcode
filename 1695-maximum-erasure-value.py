"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a,
that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""

from itertools import accumulate
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a = list(accumulate(nums, initial=0))
        seen = {}
        j = 0
        ans = 0
        for i, num in enumerate(nums):
            if num in seen:
                ans = max(ans, a[i] - a[j])
                prev_j = j
                j = seen[num] + 1
                for c1 in nums[prev_j:j]:
                    del seen[c1]
            seen[num] = i
        ans = max(ans, a[len(nums)] - a[j])
        return ans


def main():
    nums = [4, 2, 4, 5, 6]
    print(Solution().maximumUniqueSubarray(nums))


if __name__ == '__main__':
    main()

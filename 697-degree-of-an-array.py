"""
Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.



Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.


Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(SortedList)
        best_freq = 0
        for i, num in enumerate(nums):
            d[num].add(i)
            best_freq = max(best_freq, len(d[num]))
        ans = 10 ** 20
        for v in sorted(d.values(), key=len, reverse=True):
            if len(v) == best_freq:
                ans = min(ans, v[-1] - v[0] + 1)
            else:
                break
        return ans


def main():
    nums = [1, 2, 2, 3, 1]
    print(Solution().findShortestSubArray(nums))


if __name__ == '__main__':
    main()

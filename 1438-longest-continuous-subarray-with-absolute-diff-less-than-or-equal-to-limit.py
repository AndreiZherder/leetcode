"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray
such that the absolute difference between any two elements of this subarray is less than or equal to limit.



Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

"""
from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        j = 0
        maxq = deque()
        minq = deque()
        best = 0
        for i in range(n):
            while maxq and nums[maxq[-1]] <= nums[i]:
                maxq.pop()
            maxq.append(i)
            while minq and nums[minq[-1]] >= nums[i]:
                minq.pop()
            minq.append(i)
            while j <= i and nums[maxq[0]] - nums[minq[0]] > limit:
                if maxq[0] <= j:
                    maxq.popleft()
                if minq[0] <= j:
                    minq.popleft()
                j += 1
            best = max(best, i - j + 1)
        return best


def main():
    nums = [8, 2, 4, 7]
    limit = 4
    print(Solution().longestSubarray(nums, limit))


if __name__ == '__main__':
    main()

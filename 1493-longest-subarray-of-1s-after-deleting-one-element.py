"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1]
longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""
from itertools import chain
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        segments = []
        started = False
        for i, num in enumerate(chain(nums, [0])):
            if started:
                if num == 0:
                    segments.append((start, i - 1))
                    started = False
            else:
                if num == 1:
                    start = i
                    started = True
        m = len(segments)
        if not segments:
            return 0
        if m == 1:
            length = segments[0][1] - segments[0][0] + 1
            if length == len(nums):
                return length - 1
            else:
                return length
        best = segments[0][1] - segments[0][0] + 1
        for i in range(1, m):
            if segments[i][0] != segments[i - 1][1] + 2:
                best = max(best, segments[i][1] - segments[i][0] + 1)
            else:
                best = max(best, segments[i][1] - segments[i - 1][0])
        return best


def main():
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(Solution().longestSubarray(nums))


if __name__ == '__main__':
    main()

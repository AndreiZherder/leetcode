"""
There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in
non-decreasing order, where prizePositions[i] is the position of the ith prize.
There could be different prizes at the same position on the line. You are also given an integer k.

You are allowed to select two segments with integer endpoints. The length of each segment must be k.
You will collect all prizes whose position falls within at least one of the two selected segments
(including the endpoints of the segments). The two selected segments may intersect.

For example if k = 2, you can choose segments [1, 3] and [2, 4],
and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.
Return the maximum number of prizes you can win if you choose the two segments optimally.



Example 1:

Input: prizePositions = [1,1,2,2,3,3,5], k = 2
Output: 7
Explanation: In this example, you can win all 7 prizes by selecting two segments [1, 3] and [3, 5].
Example 2:

Input: prizePositions = [1,2,3,4], k = 0
Output: 2
Explanation: For this example, one choice for the segments is [3, 3] and [4, 4], and you will be able to get 2 prizes.


Constraints:

1 <= prizePositions.length <= 105
1 <= prizePositions[i] <= 109
0 <= k <= 109
prizePositions is sorted in non-decreasing order.
"""
from bisect import bisect_left
from typing import List


class Solution:
    def maximizeWin(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        neg_nums = [-num for num in nums][::-1]
        left_max_stack = [0 for i in range(n)]
        right_max_stack = [0 for i in range(n)]
        best1 = 0
        best2 = 0
        for i in range(n):
            cur = i - bisect_left(nums, nums[i] - k) + 1
            best1 = max(best1, cur)
            left_max_stack[i] = best1

            cur = i - bisect_left(neg_nums, neg_nums[i] - k) + 1
            best2 = max(best2, cur)
            right_max_stack[n - i - 1] = best2

        best = 0
        for i in range(n - 1):
            best = max(best, left_max_stack[i] + right_max_stack[i + 1])
        return best


def main():
    prizePositions = [1, 1, 2, 2, 3, 3, 5]
    k = 2
    print(Solution().maximizeWin(prizePositions, k))


if __name__ == '__main__':
    main()

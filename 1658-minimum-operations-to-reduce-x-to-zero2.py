"""
You are given an integer array nums and an integer x.
In one operation, you can either remove the leftmost or the rightmost element from the array nums
and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements
(5 operations in total) to reduce x to zero.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""
from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        pref = list(accumulate(nums))
        best = 10 ** 20
        i = bisect_left(pref, x)
        if i < n and pref[i] == x:
            best = min(best, i + 1)
        for j in range(n - 1, -1, -1):
            x -= nums[j]
            if x == 0:
                best = min(best, n - j)
                break
            elif x < 0:
                break
            i = bisect_left(pref, x)
            if i < j and pref[i] == x:
                best = min(best, n - j + i + 1)
        return best if best != 10 ** 20 else -1


def main():
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    print(Solution().minOperations(nums, x))


if __name__ == '__main__':
    main()

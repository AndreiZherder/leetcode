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

from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        a = list(accumulate(nums, initial=0))
        b = list(accumulate(reversed(nums), initial=0))
        ans = float('Inf')
        n = len(b)
        j = n - 1
        for i, num1 in enumerate(a):
            if j > n - 1 - i:
                j = n - 1 - i
            while j >= 0 and num1 + b[j] > x:
                j -= 1
            if j >= 0 and num1 + b[j] == x:
                ans = min(ans, i + j)
        return ans if ans != float('Inf') else -1


def main():
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    print(Solution().minOperations(nums, x))


if __name__ == '__main__':
    main()

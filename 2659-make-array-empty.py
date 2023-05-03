"""
You are given an integer array nums containing distinct numbers, and you can perform the following operations until the array is empty:

If the first element has the smallest value, remove it
Otherwise, put the first element at the end of the array.
Return an integer denoting the number of operations it takes to make nums empty.



Example 1:

Input: nums = [3,4,-1]
Output: 5
Example 2:

Input: nums = [1,2,4,3]
Output: 5
Example 3:

Input: nums = [1,2,3]
Output: 3
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
All values in nums are distinct.
"""
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        nums = [-10 ** 20] + nums
        n = len(nums)
        sl = SortedList(range(n))
        a = sorted((num, i) for i, num in enumerate(nums))
        ans = 0
        j = a[0][1]
        for num, i in a[1:]:
            pos1 = sl.bisect_left(j)
            pos2 = sl.bisect_left(i)
            if pos2 > pos1:
                ans += pos2 - pos1 - 1
            else:
                ans += len(sl) - pos1 - 1 + pos2
            sl.remove(j)
            j = i
        ans += n - 1
        return ans


def main():
    nums = [3, 4, -1]
    print(Solution().countOperationsToEmptyArray(nums))


if __name__ == '__main__':
    main()

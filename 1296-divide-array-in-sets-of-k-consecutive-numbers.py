"""
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets
of k consecutive numbers.

Return true if it is possible. Otherwise, return false.



Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109

"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        sl = SortedList(nums)
        for i in range(len(nums) // k):
            num = sl[0]
            for j in range(k):
                if num not in sl:
                    return False
                sl.remove(num)
                num += 1
        return True


def main():
    nums = [1, 2, 3, 3, 4, 4, 5, 6]
    k = 4
    print(Solution().isPossibleDivide(nums, k))


if __name__ == '__main__':
    main()

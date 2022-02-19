"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.



Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3


Constraints:

n == nums.length
2 <= n <= 10^5
1 <= nums[i] <= 10^9
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minimum = float('Inf')
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] *= 2
            minimum = min(minimum, nums[i])

        maxheap = [-num for num in nums]
        heapify(maxheap)
        maximum = maxheap[0]
        diff = -maximum - minimum
        while maxheap[0] % 2 == 0:
            maximum = heappop(maxheap)
            diff = min(diff, -maximum - minimum)
            maximum //= 2
            minimum = min(minimum, -maximum)
            heappush(maxheap, maximum)
        diff = min(diff, -maxheap[0] - minimum)

        return diff


def main():
    print(Solution().minimumDeviation([2, 10, 8]))


if __name__ == '__main__':
    main()

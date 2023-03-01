"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 104 <= nums[i] <= 5 * 10^4
"""
import random
from typing import List


def partition(a: List[int], l: int, r: int):
    rand = random.randrange(l, r + 1)
    a[l], a[rand] = a[rand], a[l]
    x = a[l]
    j1 = l
    j2 = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
    for i in range(l + 1, j2 + 1):
        if a[i] < x:
            j1 += 1
            a[i], a[j1] = a[j1], a[i]
    a[l], a[j1] = a[j1], a[l]
    a[j1], a[j2] = a[j2], a[j1]
    return j1, j2


def quick_sort(a: List[int], l: int, r: int):
    while l < r:
        m1, m2 = partition(a, l, r)
        if m1 - l <= r - m2:
            quick_sort(a, l, m1 - 1)
            l = m2 + 1
        else:
            quick_sort(a, m2 + 1, r)
            r = m1 - 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums) - 1)
        return nums


def main():
    nums = [5, 1, 1, 2, 0, 0]
    print(Solution().sortArray(nums))


if __name__ == '__main__':
    main()

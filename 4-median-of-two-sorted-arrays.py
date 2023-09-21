"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""
from heapq import merge
from itertools import islice
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        k = (n + m - 1) // 2
        if (n + m) % 2 == 1:
            return next(islice(merge(nums1, nums2), k, k + 1))
        else:
            g = islice(merge(nums1, nums2), k, k + 2)
            return (next(g) + next(g)) / 2


def main():
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()

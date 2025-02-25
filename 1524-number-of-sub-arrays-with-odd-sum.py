"""
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100

"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        even = 1
        odd = 0
        ans = 0
        pref = 0
        for num in arr:
            pref += num
            if pref % 2 == 0:
                ans = (ans + odd) % mod
            else:
                ans = (ans + even) % mod
            if pref % 2 == 0:
                even += 1
            else:
                odd += 1
        return ans


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().numOfSubarrays(arr))


if __name__ == '__main__':
    main()

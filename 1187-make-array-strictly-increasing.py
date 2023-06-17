"""
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero)
needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length
and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.



Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.


Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""
from bisect import bisect_right
from functools import lru_cache
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, prev: int) -> int:
            if i == len(arr1):
                return 0
            ans = 10 ** 20
            if arr1[i] > prev:
                ans = min(ans, dp(i + 1, arr1[i]))
            j = bisect_right(arr2, prev)
            if j < len(arr2):
                ans = min(ans, dp(i + 1, arr2[j]) + 1)
            return ans

        arr2.sort()
        ans = dp(0, -10 ** 20)
        return ans if ans != 10 ** 20 else -1


def main():
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 3, 2, 4]
    print(Solution().makeArrayIncreasing(arr1, arr2))


if __name__ == '__main__':
    main()

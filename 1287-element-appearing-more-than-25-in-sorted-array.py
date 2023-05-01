"""
Given an integer array sorted in non-decreasing order,
there is exactly one integer in the array that occurs more than 25% of the time, return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105
"""
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        k = n // 4
        for i in range(n - k):
            if arr[i] == arr[i + k]:
                return arr[i]
        return -1


def main():
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(Solution().findSpecialInteger(arr))


if __name__ == '__main__':
    main()

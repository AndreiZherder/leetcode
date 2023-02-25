"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        j = n - 1
        while i < j:
            if arr[i] == 0:
                j -= 1
            i += 1

        f = i == j and arr[j] == 0
        i = n - 1
        if f:
            arr[i] = arr[j]
            i -= 1
            j -= 1
        while j >= 0:
            arr[i] = arr[j]
            if arr[j] == 0:
                i -= 1
                arr[i] = 0
            j -= 1
            i -= 1


def main():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    print(Solution().duplicateZeros(arr))
    print(arr)


if __name__ == '__main__':
    main()

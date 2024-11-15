"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are
non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be
[1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element.
Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.


Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109

"""
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [-10 ** 20] + arr + [10 ** 20]
        n = len(arr)
        i = 0
        j = n - 2
        ans = len(arr) - 2
        while j > i and arr[j] >= arr[i] and arr[j] <= arr[j + 1]:
            j -= 1
        j += 1
        ans = min(ans, j - i - 1)
        i += 1
        j = max(j, i + 1)
        while i < n - 1 and arr[i] >= arr[i - 1]:
            while j < n and arr[j] < arr[i]:
                j += 1
            ans = min(ans, j - i - 1)
            i += 1
            j = max(j, i + 1)
        return ans


def main():
    arr = [1]
    print(Solution().findLengthOfShortestSubarray(arr))


if __name__ == '__main__':
    main()

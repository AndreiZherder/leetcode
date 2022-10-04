"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""
from bisect import bisect_left
from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        j = bisect_left(arr, x)
        i = j - 1
        n = len(arr)
        m = 0
        ans = deque()
        while m < k:
            if i == -1:
                ans.append(arr[j])
                j += 1
            elif j == n:
                ans.appendleft(arr[i])
                i -= 1
            elif x - arr[i] <= arr[j] - x:
                ans.appendleft(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1
            m += 1
        return list(ans)


def main():
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(Solution().findClosestElements(arr, k, x))


if __name__ == '__main__':
    main()

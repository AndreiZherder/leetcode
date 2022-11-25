"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444


Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        lefts = [0 for i in range(n)]
        rights = [0 for i in range(n)]
        stack = []
        for i, num in enumerate(arr):
            cnt = 1
            while stack and num < stack[-1][0]:
                cnt += stack.pop()[1]
            stack.append((num, cnt))
            lefts[i] = cnt - 1
        stack = []
        for i, num in enumerate(reversed(arr)):
            cnt = 1
            while stack and num <= stack[-1][0]:
                cnt += stack.pop()[1]
            stack.append((num, cnt))
            rights[n - i - 1] = cnt - 1

        ans = 0
        for i in range(n):
            left = i - lefts[i]
            right = i + rights[i]
            n = right - left + 1
            cnt = (n - (i - left)) * (i - left + 1)
            ans = (ans + cnt * arr[i]) % mod
        print(lefts, rights)
        return ans


def main():
    # arr = [3, 1, 2, 4]
    # arr = [11, 81, 94, 43, 3]
    arr = [2, 2, 2, 2, 2]
    print(Solution().sumSubarrayMins(arr))


if __name__ == '__main__':
    main()

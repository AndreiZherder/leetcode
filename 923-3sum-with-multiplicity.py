"""
Given an integer array arr, and an integer target,
return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""
from collections import defaultdict
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        p = 10 ** 9 + 7
        ans = 0
        n = len(arr)
        d = defaultdict(int)
        for i in range(2, n):
            for j in range(i - 1):
                d[arr[j] + arr[i - 1]] += 1
            ans = (ans + d[target - arr[i]]) % p
        return ans


def main():
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target = 8
    print(Solution().threeSumMulti(nums, target))


if __name__ == '__main__':
    main()

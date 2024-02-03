"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.
Test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1


Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length

"""
from functools import lru_cache
from typing import List


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/RangeQuery.py
class RangeQuery:
    """
    Range queries on a static array
    """

    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            if i >= n:
                return 0
            ans = 0
            for j in range(i, min(i + k, n)):
                ans = max(ans, rq.query(i, j + 1) * (j - i + 1) + dp(j + 1))
            return ans

        rq = RangeQuery(arr, func=max)
        n = len(arr)
        return dp(0)


def main():
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    print(Solution().maxSumAfterPartitioning(arr, k))


if __name__ == '__main__':
    main()

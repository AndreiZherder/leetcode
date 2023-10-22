"""
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1).
A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.



Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
"""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/RangeQuery.py
        class RangeQuery:
            """
            Range queries on a static array
            """

            def __init__(self, data):
                self._data = _data = [list(data)]
                i, n = 1, len(_data[0])
                while 2 * i <= n:
                    prev = _data[-1]
                    _data.append([self.func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
                    i <<= 1

            def func(self, i: int, j: int) -> int:
                if nums[i] <= nums[j]:
                    return i
                else:
                    return j

            def query(self, start, stop):
                """func of data[start, stop)"""
                depth = (stop - start).bit_length() - 1
                return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

            def __getitem__(self, idx):
                return self._data[0][idx]

        def divide_and_conquer(left: int, right: int) -> int:
            if left > k or right < k:
                return 0
            mini = rq.query(left, right + 1)
            ans1 = nums[mini] * (right - left + 1)
            ans2 = divide_and_conquer(left, mini - 1)
            ans3 = divide_and_conquer(mini + 1, right)
            return max(ans1, ans2, ans3)

        n = len(nums)
        rq = RangeQuery(range(n))
        return divide_and_conquer(0, n - 1)


def main():
    nums = [1, 4, 3, 7, 4, 5]
    k = 3
    print(Solution().maximumScore(nums, k))


if __name__ == '__main__':
    main()

"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources,
it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way
to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and
a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit
will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital,
and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6


Constraints:

1 <= k <= 10^5
0 <= w <= 10^9
n == profits.length
n == capital.length
1 <= n <= 10^5
0 <= profits[i] <= 10^4
0 <= capital[i] <= 10^9
"""
from bisect import bisect_right
from typing import List


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SegmentTree.py
class SegmentTree:
    """
    Update point, range (sum, max, min, xor ...) queries
    """

    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        s = sorted(zip(capital, profits))
        st = SegmentTree([(profit, key) for key, (capital, profit) in enumerate(s)], default=(0, 0))
        for j in range(k):
            i = bisect_right(s, (w, 10 ** 20)) - 1
            if i == -1:
                return w
            x, key = st.query(0, i + 1)
            w += x
            st[key] = (0, key)
        return w


def main():
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(Solution().findMaximizedCapital(k, w, profits, capital))


if __name__ == '__main__':
    main()

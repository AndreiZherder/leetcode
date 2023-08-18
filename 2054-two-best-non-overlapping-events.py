"""
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei].
The ith event starts at startTimei and ends at endTimei, and if you attend this event,
you will receive a value of valuei. You can choose at most two non-overlapping events
to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them
starts and the other ends at the same time. More specifically, if you attend an event with end time t,
the next event must start at or after t + 1.



Example 1:
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.


Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106

"""
from bisect import bisect_right
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
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        INF = 10 ** 20
        n = len(events)
        starts = []
        ends = []
        for i, (s, e, v) in enumerate(events):
            starts.append((s, i, v))
            ends.append((e, i, v))
        starts.sort()
        ends.sort()
        rqs = RangeQuery([start[2] for start in starts], func=max)
        rqe = RangeQuery([end[2] for end in ends], func=max)
        best = 0
        for s, i, v in starts:
            best = max(best, v)
            j = bisect_right(ends, (s, -INF, -INF))
            if j > 0:
                best = max(best, v + rqe.query(0, j))
            j = bisect_right(starts, (events[i][1], INF, INF))
            if j < n:
                best = max(best, v + rqs.query(j, n))
        return best


def main():
    events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
    print(Solution().maxTwoEvents(events))


if __name__ == '__main__':
    main()

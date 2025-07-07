"""
You are given an array of events where events[i] = [startDayi, endDayi].
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.



Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4


Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105

"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans = 0
        h = []
        i = 0
        events.sort()
        while h or i < len(events):
            if not h:
                d = events[i][0]
            while i < len(events) and events[i][0] == d:
                heappush(h, events[i][1])
                i += 1
            heappop(h)
            ans += 1
            d += 1
            while h and h[0] < d:
                heappop(h)
        return ans


def main():
    events = [[1, 2], [2, 3], [3, 4]]
    print(Solution().maxEvents(events))


if __name__ == '__main__':
    main()

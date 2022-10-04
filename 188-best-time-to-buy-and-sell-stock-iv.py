"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0)
and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def count_loss(i: int):
            (loss, prev_min_pos, prev_max_pos, next_max_pos, next_min_pos) = days[i]
            if prices[prev_max_pos] <= prices[next_max_pos]:
                loss = prices[prev_max_pos] - prices[i]
            else:
                loss = prices[next_max_pos] - prices[i]
            days[i] = (loss, prev_min_pos, prev_max_pos, next_max_pos, next_min_pos)

        if k == 0:
            return 0
        n = len(prices)
        if n <= 1:
            return 0
        prices = [float('Inf')] + prices + [-float('Inf')] + [float('Inf')]
        n = len(prices)
        days = dict()
        h = []
        versions = [0 for i in range(n)]
        prev_max_pos = 0
        prev_min_pos = -1
        go_down = True
        for i in range(1, n):
            if go_down:
                if prices[i] <= prices[i - 1]:
                    continue
                min_pos = i - 1
                if min_pos != n - 2:
                    days[min_pos] = (-1, prev_min_pos, prev_max_pos, -1, -1)
                if prev_min_pos != -1:
                    (a, b, c, d, e) = days[prev_min_pos]
                    days[prev_min_pos] = (a, b, c, prev_max_pos, min_pos)
                    count_loss(prev_min_pos)
                    versions[prev_min_pos] += 1
                    heappush(h, (days[prev_min_pos][0], prev_min_pos, versions[prev_min_pos]))
                prev_min_pos = min_pos
                go_down = False
            else:
                if prices[i] >= prices[i - 1]:
                    continue
                prev_max_pos = i - 1
                go_down = True

        cnt = len(days) - k
        while cnt > 0:
            # print(cnt, days)
            loss, i, version = heappop(h)
            if version < versions[i]:
                continue
            loss, prev_min_pos, prev_max_pos, next_max_pos, next_min_pos = days[i]
            del days[i]
            if prices[prev_max_pos] <= prices[next_max_pos]:
                if next_min_pos != n - 2:
                    (a, b, c, d, e) = days[next_min_pos]
                    days[next_min_pos] = (a, prev_min_pos, c, d, e)
                if prev_min_pos != -1:
                    (a, b, c, d, e) = days[prev_min_pos]
                    days[prev_min_pos] = (a, b, c, next_max_pos, next_min_pos)
                    count_loss(prev_min_pos)
                    versions[prev_min_pos] += 1
                    heappush(h, (days[prev_min_pos][0], prev_min_pos, versions[prev_min_pos]))
            else:
                if prev_min_pos != -1:
                    (a, b, c, d, e) = days[prev_min_pos]
                    days[prev_min_pos] = (a, b, c, d, next_min_pos)
                if next_min_pos != n - 2:
                    (a, b, c, d, e) = days[next_min_pos]
                    days[next_min_pos] = (a, prev_min_pos, prev_max_pos, d, e)
                    count_loss(next_min_pos)
                    versions[next_min_pos] += 1
                    heappush(h, (days[next_min_pos][0], next_min_pos, versions[next_min_pos]))
            cnt -= 1

        # print(cnt, days)
        ans = 0
        for i, (loss, prev_min_pos, prev_max_pos, next_max_pos, next_min_pos) in days.items():
            ans += prices[next_max_pos] - prices[i]
        return ans


def main():
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(Solution().maxProfit(k, prices))


if __name__ == '__main__':
    main()

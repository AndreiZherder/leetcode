"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, can_buy: bool) -> int:
            if i >= n:
                return 0
            if can_buy:
                return max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                return max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))

        n = len(prices)
        return dfs(0, True)


def main():
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))


if __name__ == '__main__':
    main()

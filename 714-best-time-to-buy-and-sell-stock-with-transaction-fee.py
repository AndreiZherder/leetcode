"""
You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104

"""
from typing import List
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @bootstrap
        def dp(bought: bool, i: int) -> int:
            if (bought, i) in cache:
                yield cache[(bought, i)]
            if i == n:
                yield 0
            if bought:
                ans1 = yield dp(False, i + 1)
                ans2 = yield dp(True, i + 1)
                ans = max(prices[i] + ans1, ans2)
                cache[(bought, i)] = ans
                yield ans
            else:
                ans1 = yield dp(True, i + 1)
                ans2 = yield dp(False, i + 1)
                ans = max(-prices[i] - fee + ans1, ans2)
                cache[(bought, i)] = ans
                yield ans

        cache = dict()
        return dp(False, 0)


def main():
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices, fee))


if __name__ == '__main__':
    main()

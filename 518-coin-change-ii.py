"""
You are given an integer array coins representing coins of different denominations and an integer
amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000

"""
from functools import lru_cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, amount: int) -> int:
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            return sum(dp(j, amount - coins[j]) for j in range(i, n))

        n = len(coins)
        coins.sort(reverse=True)
        return dp(0, amount)


def main():
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))


if __name__ == '__main__':
    main()

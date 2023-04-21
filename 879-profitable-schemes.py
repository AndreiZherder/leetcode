"""
There is a group of n members, and a list of various crimes they could commit.
The ith crime generates a profit[i] and requires group[i] members to participate in it.
If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit,
and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).


Constraints:

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
"""
from functools import lru_cache
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, minProfit: int, n: int) -> int:
            '''
            number of schemes to get minProfit with n members starting at crime i
            '''
            if i == m - 1:
                if n >= group[i]:
                    if profit[i] >= minProfit:
                        return 1
                    else:
                        return 0
                else:
                    return 0

            if n <= 0:
                return 0

            ans = 0
            if n >= group[i]:
                if profit[i] >= minProfit:
                    ans += 1 + dp(i + 1, max(0, minProfit - profit[i]), n - group[i])
                else:
                    ans += dp(i + 1, max(0, minProfit - profit[i]), n - group[i])
            ans += dp(i + 1, minProfit, n)
            return ans % mod

        mod = 10 ** 9 + 7
        m = len(profit)
        ans = 0
        if minProfit == 0:
            ans = 1
        return (ans + dp(0, minProfit, n)) % mod


def main():
    n = 10
    minProfit = 5
    group = [2, 3, 5]
    profit = [6, 7, 8]
    print(Solution().profitableSchemes(n, minProfit, group, profit))


if __name__ == '__main__':
    main()

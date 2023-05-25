"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points.
During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer.
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.



Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278


Constraints:

0 <= k <= n <= 104
1 <= maxPts <= 104
"""
from typing import List


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        dp = [0 for i in range(k + max(n, maxPts) + 1)]
        for i in range(k, n + 1):
            dp[i] = 1

        if k == 0:
            return dp[0]

        dp[k - 1] = sum(dp[k - 1 + j] for j in range(1, maxPts + 1)) / maxPts
        for i in range(k - 2, -1, -1):
            dp[i] = (dp[i + 1] * maxPts - dp[i + 1 + maxPts] + dp[i + 1]) / maxPts
        return dp[0]

        # @lru_cache(None)
        # def dp(points: int) -> float:
        #     if points >= k:
        #         if points <= n:
        #             return 1
        #         else:
        #             return 0
        #     else:
        #         return sum(dp(points + i) / maxPts for i in range(1, maxPts + 1))
        # return dp(0)


def main():
    n = 21
    k = 17
    maxPts = 10
    print(Solution().new21Game(n, k, maxPts))


if __name__ == '__main__':
    main()

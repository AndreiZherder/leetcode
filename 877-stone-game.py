"""
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row,
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd,
so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn,
a player takes the entire pile of stones either from the beginning or from the end of the row.
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.



Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
Example 2:

Input: piles = [3,7,2,3]
Output: true


Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.

"""
from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i == j:
                return piles[i]
            ans1 = piles[i] + pref[j + 1] - pref[i + 1] - dp(i + 1, j)
            ans2 = piles[j] + pref[j] - pref[i] - dp(i, j - 1)
            return max(ans1, ans2)

        n = len(piles)
        pref = list(accumulate(piles, initial=0))
        alice = dp(0, n - 1)
        return alice > pref[-1] - alice


def main():
    piles = [5, 3, 4, 5]
    print(Solution().stoneGame(piles))


if __name__ == '__main__':
    main()

"""
Your music player contains n different songs. You want to listen to goal songs (not necessarily different)
during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large,
return it modulo 109 + 7.



Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].


Constraints:

0 <= k < n <= goal <= 100
"""
from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return 1
            if j == 0:
                return 0
            if i < j:
                return 0
            x1 = dp(i - 1, j - 1) * (n - j + 1) % mod
            x2 = dp(i - 1, j) * (j - k) % mod if j > k else 0
            return (x1 + x2) % mod
        mod = 10 ** 9 + 7
        return dp(goal, n)


def main():
    n = 3
    goal = 3
    k = 1
    print(Solution().numMusicPlaylists(n, goal, k))


if __name__ == '__main__':
    main()

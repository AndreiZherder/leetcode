"""
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range
li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.



Example 1:
Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10.
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:
Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10.
It covers 2 white tiles, so we return 2.


Constraints:

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
The tiles are non-overlapping.

"""
from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        pref = list(accumulate((tile[1] - tile[0] + 1 for tile in tiles), initial=0))
        best = -10 ** 20
        for i in range(n):
            j = bisect_right(tiles, [tiles[i][0] + carpetLen, 10 ** 20]) - 1
            end = tiles[i][0] + carpetLen - 1
            best = max(best,  end - tiles[j][0] + 1 - max(0, end - tiles[j][1]) + pref[j] - pref[i])
        return best


def main():
    tiles = [[10, 11], [1, 1]]
    carpetLen = 2
    print(Solution().maximumWhiteTiles(tiles, carpetLen))


if __name__ == '__main__':
    main()

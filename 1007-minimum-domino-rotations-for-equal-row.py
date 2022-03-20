"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same,
or all the values in bottoms are the same.

If it cannot be done, return -1.



Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Constraints:

2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""
from collections import defaultdict
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        d = defaultdict(list)
        d[tops[0]] = [0, 0]
        if tops[0] != bottoms[0]:
            d[bottoms[0]] = [0, 0]
        for top, bottom in zip(tops, bottoms):
            for num in d.copy():
                if num != top and num != bottom:
                    d.pop(num)
                    if not d:
                        return -1
                elif top != bottom:
                    if num == top:
                        d[num][0] += 1
                    else:
                        d[num][1] += 1
        return min(list(d.values())[0][0], list(d.values())[0][1])


def main():
    tops =    [1, 2, 2, 2, 2, 1]
    bottoms = [2, 1, 1, 1, 1, 2]
    print(Solution().minDominoRotations(tops, bottoms))


if __name__ == '__main__':
    main()

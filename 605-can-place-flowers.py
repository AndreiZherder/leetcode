"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        free = 1
        ans = 0
        for flower in flowerbed:
            if not flower:
                free += 1
            else:
                ans += (free - 1) // 2
                free = 0
        free += 1
        ans += (free - 1) // 2
        return n <= ans


def main():
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 1))


if __name__ == '__main__':
    main()

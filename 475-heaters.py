"""
Winter is coming! During the contest, your first job is to design a standard heater with
a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.

Given the positions of houses and heaters on a horizontal line, return the minimum radius
standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.



Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard,
then all the houses can be warmed.
Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard,
then all the houses can be warmed.
Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3


Constraints:

1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109
"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(mid: int) -> bool:
            for h in houses:
                i = bisect_left(heaters, mid - h)
                j = bisect_right(heaters, mid + h) - 1
                if i < n and abs(h - heaters[i]) <= mid:
                    continue
                if j >= 0 and abs(h - heaters[j]) <= mid:
                    continue
                return False
            return True

        heaters.sort()
        n = len(heaters)
        left = 0
        right = max(max(heaters) - min(houses), max(houses) - min(heaters))
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


def main():
    houses = [1, 5]
    heaters = [2]
    print(Solution().findRadius(houses, heaters))


if __name__ == '__main__':
    main()

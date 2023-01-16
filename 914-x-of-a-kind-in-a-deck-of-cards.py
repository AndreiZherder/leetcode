"""
You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.



Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
"""
from collections import Counter
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        nums = list(Counter(deck).values())
        a = nums[0]
        for i in range(1, len(nums)):
            a = gcd(a, nums[i])
        return a > 1


def main():
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    print(Solution().hasGroupsSizeX(deck))


if __name__ == '__main__':
    main()

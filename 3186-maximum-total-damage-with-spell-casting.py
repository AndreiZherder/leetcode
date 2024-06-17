"""
A magician has various spells.

You are given an array power, where each element represents the damage of a spell.
Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i],
they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.



Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.



Constraints:

1 <= power.length <= 105
1 <= power[i] <= 109

"""
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        d = Counter(power)
        profit = Counter()
        prev1 = -10 ** 20
        prev2 = -10 ** 20
        prev3 = -10 ** 20
        for num in sorted(d):
            profit[num] = max(profit[prev3] + d[num] * num,
                              profit[prev2] if num - prev2 == 2 else profit[prev2] + d[num] * num,
                              profit[prev1] if num - prev1 == 1 or num - prev1 == 2 else profit[prev1] + d[num] * num)
            prev3 = prev2
            prev2 = prev1
            prev1 = num
        return profit[prev1]


def main():
    power = [1, 1, 3, 4]
    print(Solution().maximumTotalDamage(power))


if __name__ == '__main__':
    main()

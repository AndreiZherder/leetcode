"""
You are given an integer array values where values[i] represents the value of the ith sightseeing spot.
Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j:
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.



Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2


Constraints:

2 <= values.length <= 5 * 10^4
1 <= values[i] <= 1000
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        a = [num + i for i, num in enumerate(values)]
        b = [num - j for j, num in enumerate(values)]

        best = -10 ** 20
        prefix = []
        for j in range(n - 1, -1, -1):
            best = max(best, b[j])
            prefix.append(best)
        best = -10 ** 20
        for i in range(n - 1):
            best = max(best, a[i] + prefix[n - i - 2])
        return best


def main():
    values = [8, 1, 5, 2, 6]
    print(Solution().maxScoreSightseeingPair(values))


if __name__ == '__main__':
    main()

"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.

"""
from typing import List

from sortedcontainers import SortedList


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        lg, ls, rg, rs = [0] * n, [0] * n, [0] * n, [0] * n
        sl = SortedList()
        for i in range(n):
            ls[i] = sl.bisect_left(rating[i])
            lg[i] = i - ls[i]
            sl.add(rating[i])
        sl = SortedList()
        for i in range(n - 1, -1, -1):
            rs[i] = sl.bisect_left(rating[i])
            rg[i] = n - 1 - i - rs[i]
            sl.add(rating[i])
        ans = 0
        for i in range(n):
            ans += lg[i] * rs[i] + ls[i] * rg[i]
        return ans


def main():
    rating = [3, 6, 7, 5, 1]
    print(Solution().numTeams(rating))


if __name__ == '__main__':
    main()

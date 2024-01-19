"""
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n.
The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run.
You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts),
where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.



Example 1:

Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
Output: 3
Explanation:
It is possible to run all individual and consecutive pairs of robots within budget.
To obtain answer 3, consider the first 3 robots. The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24
which is less than 25.
It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.
Example 2:

Input: chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
Output: 0
Explanation: No robot can be run that does not exceed the budget, so we return 0.


Constraints:

chargeTimes.length == runningCosts.length == n
1 <= n <= 5 * 104
1 <= chargeTimes[i], runningCosts[i] <= 105
1 <= budget <= 1015

"""
from typing import List


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/RangeQuery.py
class RangeQuery:
    """
    Range queries on a static array
    """

    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        best = 0
        n = len(chargeTimes)
        j = 0
        total = 0
        rq = RangeQuery(chargeTimes, func=max)
        for i in range(n):
            total += runningCosts[i]
            while j <= i and rq.query(j, i + 1) + (i - j + 1) * total > budget:
                total -= runningCosts[j]
                j += 1
            best = max(best, i - j + 1)
        return best


def main():
    chargeTimes = [3, 6, 1, 3, 4]
    runningCosts = [2, 1, 3, 4, 5]
    budget = 25
    print(Solution().maximumRobots(chargeTimes, runningCosts, budget))


if __name__ == '__main__':
    main()

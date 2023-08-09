"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3.
If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.



Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0


Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105

"""
from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            profit = 0
            for w in worker:
                profit += pref[bisect_right(difficulty, w)]
            return profit >= mid

        h = sorted((d, p) for d, p in zip(difficulty, profit))
        difficulty = [d for d, p in h]
        profit = [p for d, p in h]
        pref = list(accumulate(profit, max, initial=0))
        left = 0
        right = len(profit) * max(profit)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


def main():
    difficulty = [85, 47, 57]
    profit = [24, 66, 99]
    worker = [40, 25, 25]
    print(Solution().maxProfitAssignment(difficulty, profit, worker))


if __name__ == '__main__':
    main()

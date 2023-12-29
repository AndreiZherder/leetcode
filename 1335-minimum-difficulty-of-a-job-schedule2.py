"""
You want to schedule a list of jobs in d days.
Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day.
The difficulty of a job schedule is the sum of difficulties of each day of the d days.
The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.



Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.


Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""
from functools import lru_cache
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
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dp(i: int, day: int) -> int:
            if n - i < d - day:
                return 10 ** 20
            if day == d:
                if i == n:
                    return 0
                else:
                    return 10 ** 20
            ans = 10 ** 20
            for j in range(i, n):
                ans = min(ans, rq.query(i, j + 1) + dp(j + 1, day + 1))
            return ans

        n = len(jobDifficulty)
        if d > n:
            return -1
        rq = RangeQuery(jobDifficulty, func=max)
        return dp(0, 0)



def main():
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    print(Solution().minDifficulty(jobDifficulty, d))


if __name__ == '__main__':
    main()

"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 10^4
1 <= time[i] <= 500
"""
from collections import Counter
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = Counter()
        ans = 0
        for song_time in time:
            num = (60 - song_time % 60) % 60
            if num in d:
                ans += d[num]
            d[song_time % 60] += 1
        return ans


def main():
    time = [60, 60, 60]
    print(Solution().numPairsDivisibleBy60(time))


if __name__ == '__main__':
    main()

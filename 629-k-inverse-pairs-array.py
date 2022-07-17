"""
For an integer array nums, an inverse pair is a pair of integers [i, j]
where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k,
return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.
Since the answer can be huge, return it modulo 10^9 + 7.



Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Constraints:

1 <= n <= 1000
0 <= k <= 1000
"""

from itertools import accumulate


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0 for i in range(k + 1)]
        dp[0] = 1
        end = 0

        for i in range(2, n + 1):
            end += i - 1
            acc = list(accumulate(dp[:end + 1], func=lambda x, y: (x + y) % mod, initial=0))
            dp1 = [0 for i in range(k + 1)]
            dp1[0] = 1
            for j in range(1, min(end, k) + 1):
                dp1[j] = (acc[j + 1] - acc[0]) % mod if j + 1 < i else (acc[j + 1] - acc[j + 1 - i]) % mod
            dp = dp1
        return dp[k]


def main():
    n = 4
    k = 7
    print(Solution().kInversePairs(n, k))


if __name__ == '__main__':
    main()

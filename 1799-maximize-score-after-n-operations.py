"""
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.



Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
"""
from functools import lru_cache
from typing import List


@lru_cache(None)
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while ((a | b) & 1) == 0:
        a = a >> 1
        b = b >> 1
        k = k + 1
    while (a & 1) == 0:
        a = a >> 1
    while b != 0:
        while (b & 1) == 0:
            b = b >> 1
        if a > b:
            a, b = b, a
        b = b - a
    return a << k


class Solution:
    def __init__(self):
        self.ans = 0

    def maxScore(self, nums: List[int]) -> int:
        def calc(cur: List[int]) -> int:
            gs = []
            for i in range(0, n, 2):
                gs.append(gcd(nums[cur[i]], nums[cur[i + 1]]))
            gs.sort()
            return sum(i * g for i, g in enumerate(gs, start=1))

        def backtrack(cur: List[int], used: int):
            if used == (1 << n) - 1:
                self.ans = max(self.ans, calc(cur))
            i = 0
            while i < n:
                if used & (1 << i) == 0:
                    cur.append(i)
                    used |= (1 << i)
                    break
                i += 1
            j = i + 1
            while j < n:
                if used & (1 << j) == 0:
                    cur.append(j)
                    used |= (1 << j)
                    backtrack(cur, used)
                    cur.pop()
                    used &= ~(1 << j)
                j += 1
            if i < n:
                cur.pop()
                used &= ~(1 << i)

        n = len(nums)
        backtrack([], 0)
        return self.ans


def main():
    nums = [1, 2, 3, 4, 5, 6]
    print(Solution().maxScore(nums))


if __name__ == '__main__':
    main()

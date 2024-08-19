"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad
for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.



Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0


Constraints:

1 <= n <= 1000

"""
from functools import lru_cache


class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def dp(i: int, buf: int) -> int:
            if i == n:
                return 0
            if i > n:
                return 10 ** 20
            ans = 10 ** 20
            if buf != 0:
                ans = min(ans, dp(i + buf, buf) + 1)
            ans = min(ans, dp(2 * i, i) + 2)
            return ans
        return dp(1, 0)


def main():
    n = 3
    print(Solution().minSteps(n))


if __name__ == '__main__':
    main()

"""
Return all non-negative integers of length n such that the absolute difference
between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.



Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Constraints:

2 <= n <= 9
0 <= k <= 9
"""
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def go(n: int, k: int, prev: int) -> List[int]:
            if n == 0:
                return [0]
            ans = []
            if k > 0:
                if prev + k < 10:
                    for num in go(n - 1, k, prev + k):
                        ans.append((prev + k) * 10 ** (n - 1) + num)
            if prev - k >= 0:
                for num in go(n - 1, k, prev - k):
                    ans.append((prev - k) * 10 ** (n - 1) + num)
            return ans
        ans = []
        for prev in range(1, 10):
            if prev - k >= 0 or prev + k < 10:
                ans.extend([prev * 10 ** (n - 1) + num for num in go(n - 1, k, prev)])
        return ans


def main():
    n = 9
    k = 1
    print(Solution().numsSameConsecDiff(n, k))


if __name__ == '__main__':
    main()

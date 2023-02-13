"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions,
you can return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 9 = n.
Note that there are other valid answers as [8, 3] that can be accepted.


Constraints:

2 <= n <= 10^4
"""
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        num = n
        i = -1
        while num:
            num //= 10
            i += 1
        if i == 0:
            a = 1
        else:
            a = 0
            for j in range(i):
                a += 10 ** j

        b = n - a
        i = 0
        while b // 10 ** i != 0:
            if (b // 10 ** i) % 10 == 0:
                b -= 10 ** i
                a += 10 ** i
            i += 1

        return [a, b]


def main():
    n = 11
    print(Solution().getNoZeroIntegers(n))


if __name__ == '__main__':
    main()

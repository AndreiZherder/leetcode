"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.



Example 1:
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1


Constraints:

0 <= n <= 10^9
"""
from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # ans = []
        # if n == 0:
        #     return 0
        # if n == 1:
        #     ans = [1]
        # a = [1 for i in range(n)]
        # for i in range(2, n + 1):
        #     a[i - 1::i] = [x ^ 1 for x in a[i - 1::i]]
        #     ans.append(a.count(1))
        # print(n, ans[-1], int(sqrt(n)))
        return int(sqrt(n))


def main():
    # for n in range(1, 101):
    #     Solution().bulbSwitch(n)
    print(Solution().bulbSwitch(15))


if __name__ == '__main__':
    main()

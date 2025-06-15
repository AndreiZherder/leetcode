"""
You are given an integer num. You will apply the following steps to num two separate times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). Note y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.



Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8


Constraints:

1 <= num <= 108

"""
from typing import List


class Solution:
    def maxDiff(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        start = 0
        if all(num[i] == num[0] for i in range(n)):
            start = 1
        mn = 10 ** 20
        mx = -10 ** 20
        for x in range(start, 10):
            for y in range(start, 10):
                cur = num[:]
                for i in range(n):
                    if cur[i] == str(x):
                        if i == 0 and (x == 0 or y == 0):
                            break
                        cur[i] = str(y)
                mn = min(mn, int(''.join(cur)))
                mx = max(mx, int(''.join(cur)))
        return mx - mn


def main():
    num = 123456
    print(Solution().maxDiff(num))


if __name__ == '__main__':
    main()

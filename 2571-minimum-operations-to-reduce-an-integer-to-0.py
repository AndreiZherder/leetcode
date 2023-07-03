"""
You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.



Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
Example 2:

Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.


Constraints:

1 <= n <= 105

"""


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)

class Solution:
    def minOperations(self, n: int) -> int:
        s = list(dec_to_bin(n, 19))
        m = len(s)
        ans = 0
        cur = 0
        for i in range(m - 1, -1, -1):
            if s[i] == '1':
                cur += 1
            elif cur > 1:
                ans += 1
                cur = 1
            elif cur == 1:
                ans += 1
                cur = 0
        return ans


def main():
    n = 39
    print(Solution().minOperations(n))


if __name__ == '__main__':
    main()

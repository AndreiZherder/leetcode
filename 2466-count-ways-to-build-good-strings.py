"""
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string,
and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties.
Since the answer can be large, return it modulo 109 + 7.



Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation:
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011".
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".


Constraints:

1 <= low <= high <= 105
1 <= zero, one <= low
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0 for i in range(high)]
        dp[zero - 1] += 1
        dp[one - 1] += 1
        for i in range(min(zero, one), high):
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % mod
        ans = 0
        for i in range(low - 1, high):
            ans = (ans + dp[i]) % mod
        return ans



def main():
    low = 2
    high = 3
    zero = 1
    one = 2
    print(Solution().countGoodStrings(low, high, zero, one))


if __name__ == '__main__':
    main()

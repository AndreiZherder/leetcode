"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1, 1, 1, 1, 1]
        prev = [1, 1, 1, 1, 1]
        for i in range(1, n):
            dp[0] = ((prev[1] + prev[2]) % mod + prev[4]) % mod
            dp[1] = (prev[0] + prev[2]) % mod
            dp[2] = (prev[1] + prev[3]) % mod
            dp[3] = prev[2]
            dp[4] = (prev[2] + prev[3]) % mod
            prev, dp = dp, prev
        ans = 0
        for num in prev:
            ans = (ans + num) % mod
        return ans


def main():
    n = 5
    print(Solution().countVowelPermutation(n))


if __name__ == '__main__':
    main()

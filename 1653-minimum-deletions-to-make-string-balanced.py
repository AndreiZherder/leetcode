"""
You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j)
such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.



Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.


Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'.

"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        def dp(i: int, prev: int) -> int:
            if cache[i][prev] != 10 ** 20:
                return cache[i][prev]
            if i == n:
                ans = 0
            else:
                ans = 10 ** 20
                if s[i] == 'a':
                    if prev == 0:
                        ans = min(ans, dp(i + 1, 0))
                    else:
                        ans = min(ans, 1 + dp(i + 1, 1))
                else:
                    if prev == 0:
                        ans = min(ans, 1 + dp(i + 1, 0))
                    ans = min(ans, dp(i + 1, 1))
            cache[i][prev] = ans
            return ans
        n = len(s)
        cache = [[10 ** 20 for j in range(2)] for i in range(n + 1)]
        return dp(0, 0)


def main():
    s = "aababbab"
    print(Solution().minimumDeletions(s))


if __name__ == '__main__':
    main()

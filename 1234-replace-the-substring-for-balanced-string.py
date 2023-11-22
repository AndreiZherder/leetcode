"""
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make
s balanced. If s is already balanced, return 0.



Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".


Constraints:

n == s.length
4 <= n <= 105
n is a multiple of 4.
s contains only 'Q', 'W', 'E', and 'R'.

"""
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        m = n // 4
        counter = Counter(s)
        unbalanced = []
        for k, v in sorted(counter.items(), key=lambda x: -x[1]):
            if v >= m:
                unbalanced.append((k, v - m))
        a, x = unbalanced[0]
        if len(unbalanced) == 2:
            unbalanced.append(('Z', 0))
        elif len(unbalanced) == 1:
            unbalanced.append(('Y', 0))
            unbalanced.append(('Z', 0))
        b, y = unbalanced[1]
        c, z = unbalanced[2]
        if x == y == z == 0:
            return 0
        i = -1
        j = 0
        best = 10 ** 20
        counter = Counter()
        while i < n:
            if counter[a] < x or counter[b] < y or counter[c] < z:
                i += 1
                if i < n:
                    counter[s[i]] += 1
                    if counter[a] >= x and counter[b] >= y and counter[c] >= z:
                        best = min(best, i - j + 1)
            else:
                while counter[a] >= x and counter[b] >= y and counter[c] >= z:
                    counter[s[j]] -= 1
                    j += 1
                    if counter[a] >= x and counter[b] >= y and counter[c] >= z:
                        best = min(best, i - j + 1)
        return best


def main():
    s = 'QQWQRRWRRQWWEWRQEREWQQWQREWRWQRQRWRQEQWE'
    print(Solution().balancedString(s))


if __name__ == '__main__':
    main()

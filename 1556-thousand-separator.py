"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"


Constraints:

0 <= n <= 2^31 - 1
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)[::-1]
        return '.'.join(s[i: i + 3] for i in range(0, len(s), 3))[::-1]


def main():
    n = 1234
    print(Solution().thousandSeparator(n))


if __name__ == '__main__':
    main()

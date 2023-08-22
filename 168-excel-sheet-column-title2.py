"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 2^31 - 1
"""
import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = string.ascii_uppercase
        ans = []
        while columnNumber:
            ans.append(s[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        return ''.join(reversed(ans))


def main():
    columnNumber = 701
    print(Solution().convertToTitle(columnNumber))


if __name__ == '__main__':
    main()

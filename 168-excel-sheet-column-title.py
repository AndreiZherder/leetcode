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



class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        orda = ord('A')
        ans = []
        while columnNumber > 0:
            rem = columnNumber % 26
            if rem == 0:
                ans.append('Z')
                columnNumber //= 26
                columnNumber -= 1
            else:
                ans.append(chr(rem - 1 + orda))
                columnNumber //= 26
        return ''.join(reversed(ans))


def main():
    columnNumber = 701
    print(Solution().convertToTitle(columnNumber))


if __name__ == '__main__':
    main()

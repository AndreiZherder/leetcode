"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.



Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0


Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9

"""


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = dec_to_bin(a, 32)
        b = dec_to_bin(b, 32)
        c = dec_to_bin(c, 32)
        ans = 0
        for x, y, z in zip(a, b, c):
            if z == '1':
                if x == '0' and y == '0':
                    ans += 1
            else:
                if x == '1':
                    ans += 1
                if y == '1':
                    ans += 1
        return ans


def main():
    a = 2
    b = 6
    c = 5
    print(Solution().minFlips(a, b, c))


if __name__ == '__main__':
    main()

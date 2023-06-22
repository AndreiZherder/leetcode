"""
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].



Example 1:

Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001.
It contains 1 on the 0th and 4th indices.
There are 2 even and 0 odd indices.
Example 2:

Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index.
There are 0 even and 1 odd indices.


Constraints:

1 <= n <= 1000
"""
from typing import List

def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = dec_to_bin(n, 0)
        return [sum(int(num) for num in s[::-1][::2]), sum(int(num) for num in s[::-1][1::2])]


def main():
    n = 17
    print(Solution().evenOddBit(n))


if __name__ == '__main__':
    main()

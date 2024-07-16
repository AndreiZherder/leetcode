"""
You are given a positive integer n.

A binary string x is valid if all
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.



Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".



Constraints:

1 <= n <= 18

"""
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(i: int, prev: str, cur: List[str]):
            if i == n:
                ans.append(''.join(cur))
                return
            if prev == '1':
                cur.append('0')
                backtrack(i + 1, '0', cur)
                cur.pop()
            cur.append('1')
            backtrack(i + 1, '1', cur)
            cur.pop()
        ans = []
        backtrack(0, '1', [])
        return ans



def main():
    n = 3
    print(Solution().validStrings(n))


if __name__ == '__main__':
    main()

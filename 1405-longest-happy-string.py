"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings,
return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.


Constraints:

0 <= a, b, c <= 100
a + b + c > 0

"""
from sortedcontainers import SortedList


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        sl = SortedList()
        if a > 0:
            sl.add((a, 'a'))
        if b > 0:
            sl.add((b, 'b'))
        if c > 0:
            sl.add((c, 'c'))
        ans = []
        prev = 'd'
        while sl:
            if len(sl) == 1:
                x = min(2, sl[0][0])
                return ''.join(ans + [x * sl[0][1]])
            else:
                if sl[-1][1] != prev:
                    cur = sl[-1]
                    sl.pop()
                    prev = cur[1]
                    x = min(2, cur[0])
                    if cur[0] > 2:
                        sl.add((cur[0] - x, cur[1]))
                    ans.append(cur[1] * x)
                else:
                    cur = sl[-2]
                    sl.pop(-2)
                    prev = cur[1]
                    x = 1
                    if cur[0] > 1:
                        sl.add((cur[0] - x, cur[1]))
                    ans.append(cur[1] * x)
        return ''.join(ans)


def main():
    a = 3
    b = 40
    c = 7
    print(Solution().longestDiverseString(a, b, c))


if __name__ == '__main__':
    main()

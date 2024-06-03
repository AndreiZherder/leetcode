"""
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters,
you can delete any of them.
Return the
lexicographically smallest
 resulting string after removing all '*' characters.



Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.



Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.

"""
from collections import defaultdict
from heapq import heappush, heappop



class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        ans = list(s)
        d = defaultdict(list)
        for i, c in enumerate(s):
            if c != '*':
                d[c].append(i)
                if len(d[c]) == 1:
                    heappush(h, c)
            else:
                ans[i] = ''
                c = heappop(h)
                ans[d[c].pop()] = ''
                if d[c]:
                    heappush(h, c)
        return ''.join(ans)



def main():
    s = "aaba*"
    print(Solution().clearStars(s))


if __name__ == '__main__':
    main()

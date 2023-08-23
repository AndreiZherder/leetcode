"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = [(-v, k) for k, v in c.items()]
        heapify(h)
        ans = []
        prev = '#'
        while h:
            v, k = heappop(h)
            if k != prev:
                ans.append(k)
                prev = k
                v += 1
                if v != 0:
                    heappush(h, (v, k))
            else:
                if not h:
                    return ''
                else:
                    v2, k2 = heappop(h)
                    ans.append(k2)
                    prev = k2
                    v2 += 1
                    if v2 != 0:
                        heappush(h, (v2, k2))
                    heappush(h, (v, k))
        return ''.join(ans)


def main():
    s = "aab"
    print(Solution().reorganizeString(s))


if __name__ == '__main__':
    main()

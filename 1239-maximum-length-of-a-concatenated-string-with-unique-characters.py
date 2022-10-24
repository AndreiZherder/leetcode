"""
You are given an array of strings arr.
A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        @lru_cache(None)
        def dfs(i: int, mask: int, length: int):
            if i == n:
                return length
            if masks[i] & mask:
                return 0
            ans = 0
            for j in range(i + 1, n + 1):
                if j not in bad:
                    ans = max(ans, dfs(j, mask | masks[i], length + len(arr[i])))
            return ans

        orda = ord('a')
        masks = []
        bad = set()
        for i, word in enumerate(arr):
            mask = 0
            for c in word:
                pos = ord(c) - orda
                if mask & (1 << pos):
                    bad.add(i)
                    break
                else:
                    mask |= (1 << pos)
            masks.append(mask)
        n = len(arr)
        ans = 0
        for i in range(n):
            if i not in bad:
                ans = max(ans, dfs(i, 0, 0))
        return ans


def main():
    arr = ["cha", "r", "act", "ers"]
    print(Solution().maxLength(arr))


if __name__ == '__main__':
    main()

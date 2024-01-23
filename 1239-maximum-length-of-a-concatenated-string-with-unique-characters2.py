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
        def backtrack(i: int, cur: int, chars: int):
            for j in range(i, n):
                if all(chars & 1 << (ord(c) - ord('a')) == 0 for c in arr[j]):
                    cur += len(arr[j])
                    ans[0] = max(ans[0], cur)
                    for c in arr[j]:
                        chars |= 1 << (ord(c) - ord('a'))
                    backtrack(j + 1, cur, chars)
                    cur -= len(arr[j])
                    for c in arr[j]:
                        chars &= ~(1 << (ord(c) - ord('a')))
        arr1 = []
        for word in arr:
            if len(set(word)) == len(word):
                arr1.append(word)
        arr = arr1
        n = len(arr)
        ans = [0]
        backtrack(0, 0, 0)
        return ans[0]



def main():
    arr = ["cha", "r", "act", "ers"]
    print(Solution().maxLength(arr))


if __name__ == '__main__':
    main()

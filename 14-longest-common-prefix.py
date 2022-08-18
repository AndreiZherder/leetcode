"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(map(len, strs))
        ans = []
        for i in range(n):
            c = strs[0][i]
            if all(str[i] == c for str in strs):
                ans.append(c)
            else:
                break
        return ''.join(ans)


def main():
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))


if __name__ == '__main__':
    main()

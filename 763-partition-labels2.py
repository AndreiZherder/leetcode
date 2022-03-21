"""
You are given a string s.
We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters."""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}
        groups = []
        for j, c in enumerate(s):
            if c not in seen:
                groups.append(1)
                seen[c] = len(groups) - 1
            else:
                group = seen[c]
                groups[group] += 1
                k = j - 1
                while s[k] != s[j]:
                    seen[s[k]] = group
                    k -= 1
                k = len(groups) - 1
                while k > group:
                    groups[group] += groups.pop()
                    k -= 1
        return groups


def main():
    s = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(s))


if __name__ == '__main__':
    main()

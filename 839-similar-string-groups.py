"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.
Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar,
but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
Notice that "tars" and "arts" are in the same group even though they are not similar.
Formally, each group is such that a word is in the group if and only
if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs.
How many groups are there?



Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1


Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""
from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        cnt += 1
                        if cnt > 2:
                            break
                if cnt == 0 or cnt == 2:
                    dsu.union(i, j)
        return len({dsu.find(i) for i in range(n)})



def main():
    strs = ["tars", "rats", "arts", "star"]
    print(Solution().numSimilarGroups(strs))


if __name__ == '__main__':
    main()

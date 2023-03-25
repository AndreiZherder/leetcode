"""
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1.
You are given a 2D integer array edges where edges[i] = [ai, bi]
denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.



Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.


Constraints:

1 <= n <= 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
"""
from collections import Counter
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for v, u in edges:
            dsu.union(v, u)
        c = Counter()
        for i in range(n):
            c[dsu.find(i)] += 1
        total = 0
        ans = 0
        for num in c.values():
            ans += num * total
            total += num
        return ans


def main():
    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    print(Solution().countPairs(n, edges))


if __name__ == '__main__':
    main()

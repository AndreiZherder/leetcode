"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1,
and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes
ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects
all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST).
An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge.
On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.



Example 1:
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges,
so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges.
We add them to the second list of the output.
Example 2:
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight,
choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.


Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.
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


def kruskal(n: int, m: int, edges: List[List[int]], deleted_edge: int, added_edge: int):
    dsu = DSU(n)
    cost = 0
    if added_edge != -1:
        _, v, u, w = edges[added_edge]
        cost = w
        dsu.union(u, v)
    for i in range(m):
        if i != deleted_edge and i != added_edge:
            _, u, v, w = edges[i]
            if dsu.find(u) != dsu.find(v):
                cost += w
                dsu.union(u, v)
    return cost


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        edges = [[i, v, u, w] for i, (v, u, w) in enumerate(edges)]
        edges.sort(key=lambda x: (x[3]))
        mst_cost = kruskal(n, m, edges, -1, -1)
        critical = []
        pseudo_critical = []
        for i in range(m):
            cost = kruskal(n, m, edges, i, -1)
            if cost > mst_cost or cost < mst_cost:
                critical.append(edges[i][0])
        for i in range(m):
            if edges[i][0] not in critical:
                cost = kruskal(n, m, edges, -1, i)
                if cost == mst_cost:
                    pseudo_critical.append(edges[i][0])
        return [critical, pseudo_critical]


def main():
    n = 5
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    print(Solution().findCriticalAndPseudoCriticalEdges(n, edges))


if __name__ == '__main__':
    main()

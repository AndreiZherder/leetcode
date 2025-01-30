"""
You are given a positive integer n representing the number of nodes in an undirected graph.
The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi]
indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x,
and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1
if it is impossible to group the nodes with the given conditions.



Example 1:
Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it,
at least on of the edges will not be satisfied.
Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group,
node 2 to the second group, and node 3 to the third group to satisfy the first two edges,
we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.


Constraints:

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.

"""
from collections import deque, defaultdict
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


def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    dsu = DSU(n)
    for v, us in enumerate(graph):
        id_v = dsu.find(v)
        if us:
            if id_v == dsu.find(us[0]):
                return False
            for i in range(1, len(us)):
                if id_v == dsu.find(us[i]):
                    return False
                dsu.union(us[i], us[i - 1])
    return True


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def bfs(v: int) -> int:
            level = 0
            q, q1 = deque([v]), deque()
            seen = {v}
            while q:
                level += 1
                while q:
                    v = q.popleft()
                    for u in g[v]:
                        if u not in seen:
                            seen.add(u)
                            q1.append(u)
                q, q1 = q1, q
            return level

        g = [[] for i in range(n)]
        for v, u in edges:
            v -= 1
            u -= 1
            g[v].append(u)
            g[u].append(v)
        if not isBipartite(g):
            return -1
        dsu = DSU(n)
        for v, u in edges:
            v -= 1
            u -= 1
            dsu.union(v, u)
        d = defaultdict(list)
        for v in range(n):
            d[dsu.find(v)].append(v)
        ans = 0
        for v in d:
            ans += max(bfs(u) for u in d[v])
        return ans


def main():
    n = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
    print(Solution().magnificentSets(n, edges))


if __name__ == '__main__':
    main()

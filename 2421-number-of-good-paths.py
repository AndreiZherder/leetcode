"""
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1
and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.
You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that
there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node
(i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example,
0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.



Example 1:
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
Example 2:
Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.
Example 3:
Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.


Constraints:

n == vals.length
1 <= n <= 3 * 10^4
0 <= vals[i] <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int):
            id1 = find(i)
            id2 = find(j)
            if id1 == id2:
                return
            if rank[id1] > rank[id2]:
                parent[id2] = id1
                cnt[id1] += cnt[id2]
                del cnt[id2]
            else:
                parent[id1] = id2
                if rank[id1] == rank[id2]:
                    rank[id2] += 1
                cnt[id2] += cnt[id1]
                del cnt[id1]

        n = len(vals)
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        d = defaultdict(list)
        for i, val in enumerate(vals):
            d[val].append(i)

        tree = defaultdict(list)
        for v, u in edges:
            tree[v].append(u)
            tree[u].append(v)

        ans = 0
        for val, nodes in sorted(d.items()):
            cnt = Counter({node: 1 for node in nodes})
            for node in nodes:
                for child in tree[node]:
                    if vals[child] <= vals[node]:
                        union(node, child)
            for m in cnt.values():
                m -= 1
                ans += m * (1 + m) // 2
        ans += n
        return ans


def main():
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    print(Solution().numberOfGoodPaths(vals, edges))


if __name__ == '__main__':
    main()

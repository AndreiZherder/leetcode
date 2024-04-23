"""
A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi]
indicates that there is an undirected edge between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]


Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs1(v: int, par: int, dist: int):
            dists[v] = dist
            for u in g[v]:
                if u != par:
                    dfs1(u, v, dist + 1)

        def dfs2(v: int, par: int, target: int, cur: List[int]) -> bool:
            if v == target:
                path[0] = cur.copy()
                return True
            for u in g[v]:
                if u != par:
                    cur.append(u)
                    if dfs2(u, v, target, cur):
                        return True
                    cur.pop()
            return False

        if n == 1:
            return [0]
        g = [[] for i in range(n)]
        for v, u in edges:
            g[v].append(u)
            g[u].append(v)

        dists = [0 for i in range(n)]
        dfs1(0, -1, 0)
        a = max(range(n), key=dists.__getitem__)

        dists = [0 for i in range(n)]
        dfs1(a, -1, 0)
        b = max(range(n), key=dists.__getitem__)

        path = [[]]
        dfs2(a, -1, b, [a])
        m = len(path[0])
        if m % 2 == 1:
            return [path[0][m // 2]]
        else:
            return [path[0][m // 2 - 1], path[0][m // 2]]


def main():
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(Solution().findMinHeightTrees(n, edges))


if __name__ == '__main__':
    main()

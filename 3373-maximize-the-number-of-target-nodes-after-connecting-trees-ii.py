"""
There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively,
where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first
tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even.
Note that a node is always target to itself.

Return an array of n integers answer, where answer[i]
is the maximum possible number of nodes that are target
to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other.
That is, for every query you will remove the added edge before proceeding to the next query.



Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

Output: [8,7,7,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 4 from the second tree.
For i = 2, connect node 2 from the first tree to node 7 from the second tree.
For i = 3, connect node 3 from the first tree to node 0 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

"""
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build(edges: List[List[int]], color: List[int]) -> List[int]:
            def dfs(v: int, par: int, depth: int, color: List[int]) -> int:
                res = 1 - depth % 2
                color[v] = depth % 2
                for u in g[v]:
                    if u != par:
                        res += dfs(u, v, depth + 1, color)
                return res

            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            ans = dfs(0, -1, 0, color)
            return [ans, n - ans]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0 for i in range(n)]
        color2 = [0 for i in range(m)]
        ans1 = build(edges1, color1)
        ans2 = build(edges2, color2)
        ans = [0 for i in range(n)]
        mx = max(ans2[0], ans2[1])
        for i in range(n):
            ans[i] = ans1[color1[i]] + mx
        return ans


def main():
    edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
    print(Solution().maxTargetNodes(edges1, edges2))


if __name__ == '__main__':
    main()

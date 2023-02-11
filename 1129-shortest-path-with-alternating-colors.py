"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1.
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x
such that the edge colors alternate along the path, or -1 if such a path does not exist.



Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]


Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [defaultdict(list), defaultdict(list)]
        for v, u in redEdges:
            graph[0][v].append(u)
        for v, u in blueEdges:
            graph[1][v].append(u)
        ans = [10 ** 20 for i in range(n)]
        seen = set()
        q = deque()
        q.append((0, 0, 0))
        q.append((0, 1, 0))
        seen.add((0, 0))
        seen.add((0, 1))
        ans[0] = 0
        while q:
            node, color, dist = q.popleft()
            for child in graph[color ^ 1][node]:
                if (child, color ^ 1) not in seen:
                    seen.add((child, color ^ 1))
                    q.append((child, color ^ 1, dist + 1))
                    ans[child] = min(ans[child], dist + 1)
        for i in range(n):
            if ans[i] == 10 ** 20:
                ans[i] = -1
        return ans


def main():
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []
    print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))


if __name__ == '__main__':
    main()

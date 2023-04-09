"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node
in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates
that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is
a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that
are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.



Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:
Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.


Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
"""
from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
        def isCyclicUtil(v, visited, recStack):

            # Mark current node as visited and
            # adds to recursion stack
            visited[v] = True
            recStack[v] = True

            # Recur for all neighbours
            # if any neighbour is visited and in
            # recStack then graph is cyclic
            for neighbour in g[v]:
                if visited[neighbour] == False:
                    if isCyclicUtil(neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True

            # The node needs to be popped from
            # recursion stack before function ends
            recStack[v] = False
            return False

        # Returns true if graph is cyclic else false
        def isCyclic():
            visited = [False] * (n + 1)
            recStack = [False] * (n + 1)
            for node in range(n):
                if visited[node] == False:
                    if isCyclicUtil(node, visited, recStack) == True:
                        return True
            return False

        @lru_cache(None)
        def dfs2(v: int) -> Counter:
            if not g[v]:
                return Counter(colors[v])
            cnt = Counter()
            for u in g[v]:
                cnt |= dfs2(u)
            cnt[colors[v]] += 1
            return cnt

        n = len(colors)
        g = [[] for i in range(n)]
        for v, u in edges:
            g[v].append(u)
        if isCyclic():
            return -1
        best = -10 ** 20
        for v in range(n):
            cnt = dfs2(v)
            best = max(best, max(cnt.values()))
        return best


def main():
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    print(Solution().largestPathValue(colors, edges))


if __name__ == '__main__':
    main()

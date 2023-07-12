"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node
if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.



Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.


Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
"""
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(v: int):
            for u in graph[v]:
                if color[u] == WHITE:
                    color[u] = GREY
                    parent[u] = v
                    dfs(u)
                    color[u] = BLACK
                elif u not in ans or color[u] == GREY:
                    cur = v
                    while cur in ans:
                        ans.remove(cur)
                        cur = parent[cur]

        n = len(graph)
        ans = set(range(n))
        WHITE = 0
        GREY = 1
        BLACK = 2
        color = [WHITE for i in range(n)]
        parent = [-1 for i in range(n)]
        for v in range(n):
            if color[v] == WHITE:
                color[v] = GREY
                dfs(v)
                color[v] = BLACK
        return sorted(ans)


def main():
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print(Solution().eventualSafeNodes(graph))


if __name__ == '__main__':
    main()

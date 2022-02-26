"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        target = (1 << n) - 1
        q = deque((node, 1 << node, 0) for node in range(n))
        seen = {(node, 1 << node) for node in range(n)}
        while q:
            node, mask, level = q.popleft()
            for neighbor in graph[node]:
                if mask | (1 << neighbor) == target:
                    return level + 1
                if (neighbor, mask | (1 << neighbor)) not in seen:
                    seen.add((neighbor, mask | (1 << neighbor)))
                    q.append((neighbor, mask | (1 << neighbor), level + 1))


def print_graph(graph: List[List[int]], node: int):
    q = deque()
    q.append(node)
    visited = {node}
    while q:
        node = q.popleft()
        print(node, [neighbor for neighbor in graph[node]])
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)


def main():
    graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print_graph(graph, 0)
    print(Solution().shortestPathLength(graph))


if __name__ == '__main__':
    main()

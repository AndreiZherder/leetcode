"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming
a network where connections[i] = [ai, bi] represents a connection between servers ai and bi.
Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]


Constraints:

2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
https://www.youtube.com/watch?v=RYaakWv5m6o&t=1500s
"""
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.node_id = 0
        self.id = []
        self.low = []
        self.visited = []
        self.ans = []

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(v: int, parent: int) -> int:
            self.visited[v] = True
            self.id[v] = self.node_id
            self.low[v] = self.node_id
            self.node_id += 1
            for to in self.graph[v]:
                if to == parent:
                    continue
                if self.visited[to]:
                    self.low[v] = min(self.low[v], self.id[to])
                else:
                    res = dfs(to, v)
                    if res > self.id[v]:
                        self.ans.append([v, to])
                    else:
                        self.low[v] = min(self.low[v], res)
            return self.low[v]
        for v, to in connections:
            self.graph[v].append(to)
            self.graph[to].append(v)
        self.id = [-1 for v in range(n)]
        self.low = [-1 for v in range(n)]
        self.visited = [False for v in range(n)]
        dfs(0, -1)
        return self.ans


def main():
    n = 4
    connections = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]
    print(Solution().criticalConnections(n, connections))


if __name__ == '__main__':
    main()

"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where
connections[i] = [ai, bi] represents a connection between computers ai and bi.
Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly
connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected.
If it is not possible, return -1.



Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.


Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
"""
from collections import Counter
from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.total = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            self.total[id1] += 1
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
            self.total[id1] += self.total[id2] + 1
        else:
            self.parent[id1] = id2
            self.total[id2] += self.total[id1] + 1
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        dsu = DSU(n)
        for v, u in connections:
            dsu.union(v, u)
        components = Counter()
        for i in range(n):
            components[dsu.find(i)] += 1
        extra = 0
        for i in components:
            extra += dsu.total[i] - (components[i] - 1)
        if extra < len(components) - 1:
            return -1
        else:
            return len(components) - 1


def main():
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    print(Solution().makeConnected(n, connections))


if __name__ == '__main__':
    main()

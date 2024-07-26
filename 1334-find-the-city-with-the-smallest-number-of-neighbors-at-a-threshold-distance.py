"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents
a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance
is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.



Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since
it has the greatest number.
Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.


Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.

"""
from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(g: List[List[Tuple[int, int]]], start: int):
            """
            Uses Dijkstra's algortihm to find the shortest path from node start
            to all other nodes in a directed weighted graph.
            """
            n = len(g)
            dist = [10 ** 20] * n
            dist[start] = 0

            q = [(0, start)]
            while q:
                cur, v = heappop(q)
                if cur == dist[v]:
                    for u, w in g[v]:
                        if cur + w < dist[u] and cur + w <= distanceThreshold:
                            dist[u] = cur + w
                            heappush(q, (cur + w, u))
            return sum(d <= distanceThreshold for d in dist)

        g = [[] for i in range(n)]
        for v, u, w in edges:
            g[v].append((u, w))
            g[u].append((v, w))
        ans = n - 1
        best = 10 ** 20
        for v in range(n - 1, -1, -1):
            cur = dijkstra(g, v)
            if cur < best:
                best = cur
                ans = v
        return ans


def main():
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4
    print(Solution().findTheCity(n, edges, distanceThreshold))


if __name__ == '__main__':
    main()

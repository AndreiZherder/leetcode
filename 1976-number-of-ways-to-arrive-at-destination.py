"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some
intersections. The inputs are generated such that you can reach any intersection from any other intersection and that
there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road
between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel
from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be
large, return it modulo 109 + 7.



Example 1:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.


Constraints:

1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
There is at most one road connecting any two intersections.
You can reach any intersection from any other intersection.

"""
from functools import lru_cache
from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
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
                        if cur + w < dist[u]:
                            dist[u] = cur + w
                            heappush(q, (cur + w, u))
            return dist

        @lru_cache(None)
        def dp(u: int) -> int:
            if u == 0:
                return 1
            ans = 0
            for v in g2[u]:
                ans = (ans + dp(v)) % mod
            return ans

        mod = 10 ** 9 + 7
        g1 = [[] for i in range(n)]
        for v, u, w in roads:
            g1[v].append((u, w))
            g1[u].append((v, w))
        dist = dijkstra(g1, 0)
        g2 = [[] for i in range(n)]
        for v in range(n):
            for u, w in g1[v]:
                if dist[u] == dist[v] + w:
                    g2[u].append(v)
        return dp(n - 1)


def main():
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
             [4, 6, 2]]
    print(Solution().countPaths(n, roads))


if __name__ == '__main__':
    main()

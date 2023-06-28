"""
You are given an undirected weighted graph of n nodes (0-indexed),
represented by an edge list where edges[i] = [a, b]
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end,
find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0.
Your answer will be accepted if it differs from the correct answer by at most 1e-5.



Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2
and the other has 0.5 * 0.5 = 0.25.
Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.


Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def dfs(v: int) -> bool:
            ans = False
            if v == end:
                return True
            else:
                for u, p in g[v]:
                    if u not in seen:
                        seen.add(u)
                        ans |= dfs(u)
            return ans

        g = defaultdict(list)
        for (v, u), p in zip(edges, succProb):
            g[v].append((u, p))
            g[u].append((v, p))

        seen = {start}
        if not dfs(start):
            return 0

        h = [(0, 1, start)]
        seen = {start}
        while h:
            no, yes, v = heappop(h)
            seen.add(v)
            if v == end:
                return 1 - no
            for u, p in g[v]:
                if u not in seen:
                    heappush(h, (1 - yes * p, yes * p, u))
        return 0


def main():
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    print(Solution().maxProbability(n, edges, succProb, start, end))


if __name__ == '__main__':
    main()

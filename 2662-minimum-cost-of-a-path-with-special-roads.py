"""
You are given an array start where start = [startX, startY] represents your initial position (startX, startY)
in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position
(targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where
specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you
from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).



Example 1:

Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
- (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
- (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
- (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
So the total cost is 1 + 2 + 1 + 1 = 5.
It can be shown that we cannot achieve a smaller total cost than 5.
Example 2:

Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special edges and go directly from the starting
to the ending position with a cost |5 - 3| + |7 - 2| = 7.


Constraints:

start.length == target.length == 2
1 <= startX <= targetX <= 105
1 <= startY <= targetY <= 105
1 <= specialRoads.length <= 200
specialRoads[i].length == 5
startX <= x1i, x2i <= targetX
startY <= y1i, y2i <= targetY
1 <= costi <= 105

"""
from heapq import heappop, heappush
from typing import List, Tuple


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


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads.append(
            [start[0], start[1], target[0], target[1], abs(target[0] - start[0]) + abs(target[1] - start[1])])
        n = len(specialRoads) * 2
        g = [[] for v in range(n)]
        for i, (_, _, _, _, cost) in enumerate(specialRoads):
            g[i * 2].append((i * 2 + 1, cost))
        for i in range(len(specialRoads) - 1):
            x1, y1, _, _, _ = specialRoads[i]
            g[n - 2].append((i * 2, abs(start[0] - x1) + abs(start[1] - y1)))
            _, _, x1, y1, _ = specialRoads[i]
            g[i * 2 + 1].append((n - 1, abs(target[0] - x1) + abs(target[1] - y1)))
            for j in range(len(specialRoads) - 1):
                if i != j:
                    x2, y2, _, _, _ = specialRoads[j]
                    g[i * 2 + 1].append((j * 2, abs(x2 - x1) + abs(y2 - y1)))
        return dijkstra(g, n - 2)[n - 1]


def main():
    start = [1, 1]
    target = [4, 5]
    specialRoads = [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]
    print(Solution().minimumCost(start, target, specialRoads))


if __name__ == '__main__':
    main()

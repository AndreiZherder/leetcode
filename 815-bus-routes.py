"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence
1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target.
You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        lookup = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                lookup[stop].append(i)
        target_routes = set(lookup[target])
        n = len(routes)
        g = [[] for i in range(n)]
        for vs in lookup.values():
            for i in range(len(vs)):
                for j in range(i + 1, len(vs)):
                    g[vs[i]].append(vs[j])
                    g[vs[j]].append(vs[i])
        q = deque()
        seen = set()
        for v in lookup[source]:
            if v in target_routes:
                return 1
            q.append((v, 1))
            seen.add(v)
        while q:
            v, buses = q.popleft()
            for u in g[v]:
                if u not in seen:
                    if u in target_routes:
                        return buses + 1
                    q.append((u, buses + 1))
                    seen.add(u)
        return -1


def main():
    routes = [[25, 33], [3, 5, 13, 22, 23, 29, 37, 45, 49], [15, 16, 41, 47], [5, 11, 17, 23, 33],
              [10, 11, 12, 29, 30, 39, 45], [2, 5, 23, 24, 33], [1, 2, 9, 19, 20, 21, 23, 32, 34, 44], [7, 18, 23, 24],
              [1, 2, 7, 27, 36, 44], [7, 14, 33]]
    source = 7
    target = 47
    print(Solution().numBusesToDestination(routes, source, target))


if __name__ == '__main__':
    main()

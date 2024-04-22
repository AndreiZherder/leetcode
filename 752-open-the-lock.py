"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around:
for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns
required to open the lock, or -1 if it is impossible.



Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.


Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

"""
from heapq import heappop, heappush
from typing import List, Tuple


def dijkstra(g: List[List[Tuple[int, int]]], start: int):
    """
    Uses Dijkstra's algortihm to find the shortest path from node start
    to all other nodes in a directed weighted graph.
    """
    n = len(g)
    dist, parent = [10 ** 20] * n, [-1] * n
    dist[start] = 0

    q = [(0, start)]
    while q:
        cur, v = heappop(q)
        if cur == dist[v]:
            for u, w in g[v]:
                if cur + w < dist[u]:
                    dist[u], parent[u] = cur + w, v
                    heappush(q, (cur + w, u))
    return dist, parent


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(int(deadend) for deadend in deadends)
        n = 10000
        g = [[] for i in range(n)]
        for i in range(n):
            if i not in deadends:
                for j in range(4):
                    ni = list(str(i).zfill(4))
                    if ni[j] == '9':
                        ni[j] = '0'
                    else:
                        ni[j] = str(int(ni[j]) + 1)
                    ni = int(''.join(ni))
                    if ni not in deadends:
                        g[i].append((ni, 1))
                        g[ni].append((i, 1))
        dist, _ = dijkstra(g, 0)
        if dist[int(target)] == 10 ** 20:
            return -1
        else:
            return dist[int(target)]


def main():
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(Solution().openLock(deadends, target))


if __name__ == '__main__':
    main()

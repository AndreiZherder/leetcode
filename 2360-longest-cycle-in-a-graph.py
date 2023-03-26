"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge
from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.



Example 1:
Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.


Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
"""
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(i: int, depth: int) -> int:
            if i == -1:
                return -1
            if i in seen:
                return -1
            if i in cur:
                return depth - cur[i]
            cur[i] = depth
            return dfs(edges[i], depth + 1)

        n = len(edges)

        seen = set()
        ans = -1
        for i in range(n):
            if i not in seen:
                cur = dict()
                ans = max(ans, dfs(i, 0))
                seen |= set(cur)
        return ans

def main():
    edges = [3, 3, 4, 2, 3]
    print(Solution().longestCycle(edges))


if __name__ == '__main__':
    main()

"""
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item
belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed.
A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that
should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.



Example 1:
Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.


Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
"""
from collections import defaultdict
from typing import List


def kahn_toposort(g) -> (List[int], List[int], bool):
    """
    Kahn topological sort
    returns:
    - topologically sorted nodes of directed graph;
    - acyclicity of graph
    takes g (adjacency list) as input
    """
    n = len(g)
    indeg = defaultdict(int)
    for v in g:
        for u in g[v]:
            indeg[u] += 1
    q, ans = [], []
    for v in g:
        if indeg[v] == 0:
            q.append(v)
    cnt = 0
    while q:
        v = q.pop()
        ans.append(v)
        cnt += 1
        for u in g[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    acyclicity = cnt == n
    return ans, acyclicity


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # assign group numbers to groupless items
        # build graph between groups, topologicaly sort it and check for acyclicity
        # in order of groups build graph between items of group
        # topologicaly sort it, check for acyclicity, add resulting list of items to answer

        d = dict()
        for i, g in enumerate(group):
            if g == -1:
                d[i] = m
                m += 1
            else:
                d[i] = g

        group_graph = {i: set() for i in range(m)}
        graphs = [dict() for i in range(m)]
        for i in range(n):
            graphs[d[i]][i] = set()

        for i, parents in enumerate(beforeItems):
            for p in parents:
                if d[p] != d[i]:
                    group_graph[d[p]].add(d[i])
                else:
                    graphs[d[p]][p].add(i)

        sorted_groups, acyclicity = kahn_toposort(group_graph)
        if not acyclicity:
            return []

        ans = []
        for g in sorted_groups:
            sorted_items, acyclicity = kahn_toposort(graphs[g])
            if not acyclicity:
                return []
            ans.extend(sorted_items)

        return ans


def main():
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    print(Solution().sortItems(n, m, group, beforeItems))


if __name__ == '__main__':
    main()

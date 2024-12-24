"""
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively.
You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1,
respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree
and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.



Example 1:
Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

Output: 3

Explanation:

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:
Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Output: 5

Explanation:

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.



Constraints:

1 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.

"""
from collections import defaultdict
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # Function to find the diameter of a tree given its edges
        # https://algo.monster/liteproblems/1245
        def tree_diameter(edges: List[List[int]]) -> int:
            if not edges:
                return 0

            # Helper function to perform a depth-first search (DFS)
            def dfs(node, distance):
                nonlocal max_diameter, visited, graph, next_node
                if visited[node]:  # If this node has already been visited, skip
                    return
                visited[node] = True
                for neighbor in graph[node]:
                    dfs(neighbor, distance + 1)  # DFS on connected nodes

                # Update the diameter and the next node if we found a longer path
                if max_diameter < distance:
                    max_diameter = distance
                    next_node = node

            # Convert the edge-list to an adjacency list representation for the graph
            graph = defaultdict(set)
            # Initialize a visited list to keep track of visited nodes during DFS
            visited = [False] * (len(edges) + 1)
            # Establish the adjacency list from the edges
            for u, v in edges:
                graph[u].add(v)
                graph[v].add(u)

            max_diameter = 0  # Initialize the diameter of the tree
            next_node = 0  # This variable will hold one end of the maximum diameter

            # Perform the first DFS to find one end of the maximum diameter path
            dfs(edges[0][0], 0)

            # Reset the visited list for the next DFS
            visited = [False] * (len(edges) + 1)

            # Perform the second DFS from the farthest node found in the first DFS
            dfs(next_node, 0)

            # The maximum distance found during the second DFS is the tree diameter
            return max_diameter

        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)

        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)


def main():
    edges1 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
    print(Solution().minimumDiameterAfterMerge(edges1, edges2))


if __name__ == '__main__':
    main()

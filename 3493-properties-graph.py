"""
You are given a 2D integer array properties having dimensions n x m and an integer k.

Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.

Construct an undirected graph where each index i corresponds to properties[i].
There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k,
where i and j are in the range [0, n - 1] and i != j.

Return the number of connected components in the resulting graph.



Example 1:

Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1

Output: 3

Explanation:

The graph formed has 3 connected components:
Example 2:

Input: properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2

Output: 1

Explanation:

The graph formed has 1 connected component:
Example 3:

Input: properties = [[1,1],[1,1]], k = 2

Output: 2

Explanation:

intersect(properties[0], properties[1]) = 1, which is less than k.
This means there is no edge between properties[0] and properties[1] in the graph.



Constraints:

1 <= n == properties.length <= 100
1 <= m == properties[i].length <= 100
1 <= properties[i][j] <= 100
1 <= k <= m
"""
from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        properties = [set(x) for x in properties]
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                if len(properties[i] & properties[j]) >= k:
                    dsu.union(i, j)
        return len({dsu.find(i) for i in range(n)})


def main():
    properties = [[1, 2, 3], [2, 3, 4], [4, 3, 5]]
    k = 2
    print(Solution().numberOfComponents(properties, k))


if __name__ == '__main__':
    main()

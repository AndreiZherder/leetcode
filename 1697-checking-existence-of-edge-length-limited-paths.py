"""
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi]
denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j]
whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer
is true if there is a path for queries[j] is true, and false otherwise.



Example 1:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping
edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2,
thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5,
thus we return true for this query.
Example 2:Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.


Constraints:

2 <= n <= 10^5
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.

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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        n = len(edgeList)
        m = len(queries)
        ans = [False for i in range(m)]
        edgeList.sort(key=lambda x: x[2])
        queries = [(i, *query) for i, query in enumerate(queries)]
        queries.sort(key=lambda x: x[3])
        pos = 0
        for k, x, y, dist in queries:
            while pos < n and edgeList[pos][2] < dist:
                dsu.union(edgeList[pos][0], edgeList[pos][1])
                pos += 1
            ans[k] = dsu.find(x) == dsu.find(y)
        return ans


def main():
    n = 5
    edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries = [[0, 4, 14], [1, 4, 13]]
    print(Solution().distanceLimitedPathsExist(n, edgeList, queries))


if __name__ == '__main__':
    main()

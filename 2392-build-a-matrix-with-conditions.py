"""
You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once.
The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number
belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears
for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.



Example 1:
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
Example 2:

Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.


Constraints:

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 104
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
"""
from typing import List


def kahn_toposort(g: List[List[int]]) -> (List[int], bool):
    """
    Kahn topological sort
    returns:
    - topologically sorted nodes of directed graph;
    - acyclicity of graph
    takes g (adjacency list) as input
    """
    n = len(g)
    indeg = [0] * n
    for v in range(n):
        for u in g[v]:
            indeg[u] += 1
    q, ans = [], []
    for v in range(n):
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
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0 for j in range(k)] for i in range(k)]
        row_graph = [[] for i in range(k)]
        col_graph = [[] for i in range(k)]
        for v, u in rowConditions:
            v -= 1
            u -= 1
            row_graph[v].append(u)
        for v, u in colConditions:
            v -= 1
            u -= 1
            col_graph[v].append(u)
        row_nums, acyclicity = kahn_toposort(row_graph)
        if not acyclicity:
            return []
        col_nums, acyclicity = kahn_toposort(col_graph)
        if not acyclicity:
            return []
        d = {num: j for j, num in enumerate(col_nums)}
        for i, num in enumerate(row_nums):
            ans[i][d[num]] = num + 1
        return ans


def main():
    k = 3
    rowConditions = [[1,2],[3,2]]
    colConditions = [[2,1],[3,2]]
    print(Solution().buildMatrix(k, rowConditions, colConditions))


if __name__ == '__main__':
    main()

"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int):
            id1 = find(i)
            id2 = find(j)
            if rank[id1] > rank[id2]:
                parent[id2] = id1
            else:
                parent[id1] = id2
                if rank[id1] == rank[id2]:
                    rank[id2] += 1

        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len({find(i) for i in range(n)})


def main():
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))


if __name__ == '__main__':
    main()

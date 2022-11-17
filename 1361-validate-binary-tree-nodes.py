"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i],
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.



Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false


Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 10^4
-1 <= leftChild[i], rightChild[i] <= n - 1
"""
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> bool:
            id1 = find(i)
            id2 = find(j)
            if id1 == id2:
                return False
            if rank[id1] > rank[id2]:
                parent[id2] = id1
            else:
                parent[id1] = id2
                if rank[id1] == rank[id2]:
                    rank[id2] += 1
            return True

        n = len(leftChild)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        seen = set()
        for v, u in enumerate(leftChild):
            if u != -1:
                seen.add(u)
                if not union(v, u):
                    return False

        for v, u in enumerate(rightChild):
            if u != -1:
                if u in seen:
                    return False
                if not union(v, u):
                    return False

        return True if len({find(i) for i in range(n)}) == 1 else False


def main():
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [2, -1, -1, -1]
    print(Solution().validateBinaryTreeNodes(n, leftChild, rightChild))


if __name__ == '__main__':
    main()

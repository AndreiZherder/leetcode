"""
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8
"""
from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs(l: int, r: int) -> List[Optional[TreeNode]]:
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            ans = []
            for i in range(l, r + 1):
                lefts = dfs(l, i - 1)
                rights = dfs(i + 1, r)
                for left in lefts:
                    for right in rights:
                        ans.append(TreeNode(i, left, right))
            return ans
        return dfs(1, n)


def main():
    n = 3
    print(Solution().generateTrees(n))


if __name__ == '__main__':
    main()

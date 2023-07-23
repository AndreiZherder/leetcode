"""
Given an integer n, return a list of all possible full binary trees with n nodes.
Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.



Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]


Constraints:

1 <= n <= 20
"""
from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def backtrack(n: int) -> List[Optional[TreeNode]]:
            if n == 1:
                return [TreeNode(0)]

            ans = []
            for i in range(1, n, 2):
                lefts = backtrack(i)
                rights = backtrack(n - 1 - i)
                for l in lefts:
                    for r in rights:
                        ans.append(TreeNode(0, l, r))
            return ans

        if n % 2 == 0:
            return None
        return backtrack(n)


def main():
    n = 5
    print(Solution().allPossibleFBT(n))


if __name__ == '__main__':
    main()

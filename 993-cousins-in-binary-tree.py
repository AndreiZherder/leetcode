"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y,
return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.



Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
"""
from typing import Optional, List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        lines, *_ = self.__display_aux()
        return '\n'.join(lines)

    def __display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if not self.right and not self.left:
            line = f"{self.val}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if not self.right:
            lines, n, p, x = self.left.__display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if not self.left:
            lines, n, p, x = self.right.__display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.__display_aux()
        right, m, q, y = self.right.__display_aux()
        s = f"{self.val}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(root: TreeNode, parent: TreeNode, depth: int, target: int) -> [bool, TreeNode, int]:
            if root.val == target:
                return (True, parent, depth)
            if root.left:
                ans = dfs(root.left, root, depth + 1, target)
                if ans[0]:
                    return ans
            if root.right:
                ans = dfs(root.right, root, depth + 1, target)
                if ans[0]:
                    return ans
            return (False, None, -1)

        ans1 = dfs(root, None, 0, x)
        ans2 = dfs(root, None, 0, y)
        return ans1[0] and ans2[0] and ans1[1] != ans2[1] and ans1[2] == ans2[2]


def main():
    vals = [1, 2, 3, None, 4, None, 5]
    x = 5
    y = 4
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    root = nodes[0] if nodes else None
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None
            node.right = nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None
    print(root)
    print(Solution().isCousins(root, x, y))


if __name__ == '__main__':
    main()

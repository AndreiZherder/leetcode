"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child
subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number
of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent
or false otherwise.



Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false


Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False
        if root1.left and root1.right:
            if not root2.left or not root2.right:
                return False
            else:
                if sorted((root1.left.val, root1.right.val)) != sorted((root2.left.val, root2.right.val)):
                    return False
                elif root1.left.val == root2.left.val:
                    return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
                elif root1.left.val == root2.right.val:
                    return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        elif root1.left:
            if root2.left and root2.right:
                return False
            elif not root2.left and not root2.right:
                return False
            elif root2.left:
                if root1.left.val != root2.left.val:
                    return False
                else:
                    return self.flipEquiv(root1.left, root2.left)
            else:
                if root1.left.val != root2.right.val:
                    return False
                else:
                    return self.flipEquiv(root1.left, root2.right)
        elif root1.right:
            if root2.left and root2.right:
                return False
            elif not root2.left and not root2.right:
                return False
            elif root2.left:
                if root1.right.val != root2.left.val:
                    return False
                else:
                    return self.flipEquiv(root1.right, root2.left)
            else:
                if root1.right.val != root2.right.val:
                    return False
                else:
                    return self.flipEquiv(root1.right, root2.right)
        elif root2.left or root2.right:
            return False
        return True


def main():
    vals1 = [0, 1, 4, 2, None, 7, None, 3, 6, None, None, None, None, None, None, 5]
    vals2 = [0, 4, 1, 7]
    nodes1 = [TreeNode(val) if val is not None else None for val in vals1]
    nodes2 = [TreeNode(val) if val is not None else None for val in vals2]
    root1 = nodes1[0] if nodes1 else None
    for i, node in enumerate(nodes1):
        if node:
            node.left = nodes1[i * 2 + 1] if i * 2 + 1 < len(nodes1) else None
            node.right = nodes1[i * 2 + 2] if i * 2 + 2 < len(nodes1) else None
    root2 = nodes2[0] if nodes2 else None
    for i, node in enumerate(nodes2):
        if node:
            node.left = nodes2[i * 2 + 1] if i * 2 + 1 < len(nodes2) else None
            node.right = nodes2[i * 2 + 2] if i * 2 + 2 < len(nodes2) else None
    print(root1)
    print(root2)
    print(Solution().flipEquiv(root1, root2))


if __name__ == '__main__':
    main()

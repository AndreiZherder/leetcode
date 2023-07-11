"""
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.



Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs2(root: TreeNode, k: int):
            if k == 1:
                ans.append(root.val)
            else:
                if root.left:
                    dfs2(root.left, k - 1)
                if root.right:
                    dfs2(root.right, k - 1)

        def dfs(root: TreeNode) -> int:
            if root == target:
                if k == 0:
                    ans.append(root.val)
                    return 1
                if root.left:
                    dfs2(root.left, k)
                if root.right:
                    dfs2(root.right, k)
                return 1
            if not root.left and not root.right:
                return -1
            depth_left = -1
            depth_right = -1
            if root.left:
                depth_left = dfs(root.left)
                if depth_left > 0:
                    if depth_left == k:
                        ans.append(root.val)
                    elif depth_left < k and root.right:
                        dfs2(root.right, k - depth_left)
                    return depth_left + 1
            if root.right and (not root.left or depth_left == -1):
                depth_right = dfs(root.right)
                if depth_right > 0:
                    if depth_right == k:
                        ans.append(root.val)
                    elif depth_right < k and root.left:
                        dfs2(root.left, k - depth_right)
                    return depth_right + 1
            return -1

        ans = []
        dfs(root)
        return ans


def main():
    vals = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    k = 2
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    target = nodes[1]
    root = nodes[0] if nodes else None
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None
            node.right = nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None
    print(root)
    print(Solution().distanceK(root, target, k))


if __name__ == '__main__':
    main()

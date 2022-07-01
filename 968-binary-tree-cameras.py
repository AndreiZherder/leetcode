"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node
can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.
The above image shows one of the valid configurations of camera placement.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val == 0
"""
from collections import namedtuple
from typing import Optional


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

Info = namedtuple('Info', 'camera, filmed, cnt')

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> Info:
            if not node.left and not node.right:
                return 0, 0, 0
            elif node.left and node.right:
                left_camera, left_filmed, left_cnt = dfs(node.left)
                right_camera, right_filmed, right_cnt = dfs(node.right)
                if left_filmed and right_filmed:
                    if left_camera or right_camera:
                        return 0, 1, left_cnt + right_cnt
                    else:
                        if node == root:
                            return 1, 1, left_cnt + right_cnt + 1
                        return 0, 0, left_cnt + right_cnt
                else:
                    return 1, 1, left_cnt + right_cnt + 1
            else:
                child = node.left if node.left else node.right
                camera, filmed, cnt = dfs(child)
                if filmed:
                    if camera:
                        return 0, 1, cnt
                    else:
                        if node == root:
                            return 1, 1, cnt + 1
                        return 0, 0, cnt
                else:
                    return 1, 1, cnt + 1

        if not root.left and not root.right:
            return 1

        camera, filmed, cnt = dfs(root)
        return cnt


def main():
    # vals = [0,
    #         0, None,
    #         None, 0, None, None,
    #         None, None, 0, None, None, None, None, None,
    #         None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None]
    # vals = [0]
    # vals = [0, 0, None, 0, 0, None, None]
    # vals = [0, 0]
    # vals = [0, 0, None, 0, None, None, None]
    # vals = [0, 0, None, 0, None, None, None, 0, None, None, None, None, None, None, None]
    # vals = [0, 0, None, 0, None, None, None,
    #         0, None, None, None, None, None, None, None,
    #         0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    # vals = [0, 0, None, 0, None, None, None,
    #         0, None, None, None, None, None, None, None,
    #         0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    #         0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    # vals = [0, 0, 0]
    vals = [0, 0, 0, None, 0, 0, None]
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    root = nodes[0] if nodes else None
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None
            node.right = nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None
    print(root)
    print(Solution().minCameraCover(root))


if __name__ == '__main__':
    main()

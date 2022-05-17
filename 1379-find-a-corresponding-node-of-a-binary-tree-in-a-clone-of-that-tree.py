"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.



Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:
Input: tree = [7], target =  7
Output: 7
Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.


Follow up: Could you solve the problem if repeated values on the tree are allowed?
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    def __init__(self):
        self.path = []

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs([], original, target)
        node = cloned
        for direction in self.path:
            if direction == 0:
                node = node.left
            else:
                node = node.right
        return node

    def dfs(self, path: List[int], node: TreeNode, target: TreeNode):
        if not node:
            return False
        if node == target:
            self.path = path
            return True
        if self.dfs(path + [0], node.left, target):
            return True
        return self.dfs(path + [1], node.right, target)


def main():
    vals = [7, 4, 3, None, None, 6, 19]
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    original = nodes[0] if nodes else None
    target = nodes[5] if nodes else None
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None
            node.right = nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None
    cloned_nodes = nodes.copy()
    cloned = cloned_nodes[0] if cloned_nodes else None
    for i, node in enumerate(cloned_nodes):
        if node:
            node.left = cloned_nodes[i * 2 + 1] if i * 2 + 1 < len(cloned_nodes) else None
            node.right = cloned_nodes[i * 2 + 2] if i * 2 + 2 < len(cloned_nodes) else None
    print(original)
    print(cloned)
    print(Solution().getTargetCopy(original, cloned, target))


if __name__ == '__main__':
    main()

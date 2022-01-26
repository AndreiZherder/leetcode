"""
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:
The number of nodes in each tree is in the range [0, 5000].
-10^5 <= Node.val <= 10^5
"""
from typing import List


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


def inorder(node: TreeNode):
    if not node:
        return
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.val
            node = node.right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        tree1 = inorder(root1)
        tree2 = inorder(root2)
        try:
            a = next(tree1)
        except StopIteration:
            ans.extend(list(tree2))
            return ans
        try:
            b = next(tree2)
        except StopIteration:
            ans.append(a)
            ans.extend(list(tree1))
            return ans

        while True:
            if a <= b:
                ans.append(a)
                try:
                    a = next(tree1)
                except StopIteration:
                    ans.append(b)
                    ans.extend(list(tree2))
                    break
            else:
                ans.append(b)
                try:
                    b = next(tree2)
                except StopIteration:
                    ans.append(a)
                    ans.extend(list(tree1))
                    break
        return ans


def main():
    left = None
    right = TreeNode(8)
    root1 = TreeNode(1, left, right)
    left = TreeNode(1)
    right = None
    root2 = TreeNode(8, left, right)
    print(*inorder(root1))
    print(*inorder(root2))
    print(root1)
    print(root2)
    print(Solution().getAllElements(root1, root2))


if __name__ == '__main__':
    main()

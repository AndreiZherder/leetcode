"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins.
There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.



Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].
Then, we move one coin from the root of the tree to the right child.


Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode) -> (int, List[int], List[int]):
            if not root:
                return 0, [], []
            lacks = []
            extra = []
            ans = 0
            if root.val == 0:
                lacks.append(0)
            elif root.val > 1:
                extra.extend([0] * (root.val - 1))

            ans_left, lacks_left, extra_left = dfs(root.left)
            ans += ans_left
            extra += [x + 1 for x in extra_left]
            lacks += [x + 1 for x in lacks_left]

            ans_right, lacks_right, extra_right = dfs(root.right)
            ans += ans_right
            extra += [x + 1 for x in extra_right]
            lacks += [x + 1 for x in lacks_right]

            if len(extra) < len(lacks):
                while extra:
                    ans += extra.pop() + lacks.pop()
            else:
                while lacks:
                    ans += extra.pop() + lacks.pop()
            return ans, lacks, extra

        return dfs(root)[0]



def main():
    vals = [0, 3, 0]
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    root = nodes[0] if nodes else None
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None
            node.right = nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None
    print(root)
    print(Solution().distributeCoins(root))


if __name__ == '__main__':
    main()

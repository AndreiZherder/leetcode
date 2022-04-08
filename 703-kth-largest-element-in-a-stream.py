"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream
and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
from typing import List


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None):
        self.val = val
        self.size = 1
        self.height = 0
        self.left = left
        self.right = right
        self.parent = parent

    def add(self, val: int):
        if val < self.val:
            if not self.left:
                self.left = Node(val, parent=self)
                self.left.update()
                node = self.left
                ret = node
                while node:
                    node = node.balance(node)
                    ret = node
                    node = node.parent
                return ret
            else:
                return self.left.add(val)
        else:
            if not self.right:
                self.right = Node(val, parent=self)
                self.right.update()
                node = self.right
                ret = node
                while node:
                    node = node.balance(node)
                    ret = node
                    node = node.parent
                return ret
            else:
                return self.right.add(val)

    def get(self, k: int) -> int:
        size = self.size - (self.left.size if self.left else 0)
        if k == size:
            return self.val
        elif k < size:
            return self.right.get(k)
        else:
            return self.left.get(k - size)

    def update(self):
        node = self
        while node:
            if node.left:
                if node.right:
                    node.height = 1 + max(node.left.height, node.right.height)
                    node.size = 1 + node.left.size + node.right.size
                else:
                    node.height = 1 + node.left.height
                    node.size = 1 + node.left.size
            elif node.right:
                node.height = 1 + node.right.height
                node.size = 1 + node.right.size
            else:
                node.height = 0
                node.size = 1
            node = node.parent

    def balance_factor(self, node: 'Node') -> int:
        return (node.right.height if node.right else 0) - (node.left.height if node.left else 0)

    def balance(self, node: 'Node') -> 'Node':
        ret = node
        if self.balance_factor(node) >= 2:
            if self.balance_factor(node.right) < 0:
                self.rotateright(node.right)
            ret = self.rotateleft(node)
            while self.balance_factor(node) >= 2:
                if self.balance_factor(node.right) < 0:
                    self.rotateright(node.right)
                self.rotateleft(node)
        if self.balance_factor(node) <= -2:
            if self.balance_factor(node.left) > 0:
                self.rotateleft(node.left)
            ret = self.rotateright(node)
            while self.balance_factor(node) <= -2:
                if self.balance_factor(node.left) > 0:
                    self.rotateleft(node.left)
                self.rotateright(node)
        return ret

    def rotateright(self, p: 'Node') -> 'Node':
        q = p.left
        p.left = q.right
        if q.right:
            q.right.parent = p
        q.right = p
        q.parent = p.parent
        p.parent = q
        if q.parent:
            if q.parent.left == p:
                q.parent.left = q
            else:
                q.parent.right = q
        p.update()
        return q

    def rotateleft(self, q: 'Node') -> 'Node':
        p = q.right
        q.right = p.left
        if p.left:
            p.left.parent = q
        p.left = q
        p.parent = q.parent
        q.parent = p
        if p.parent:
            if p.parent.left == q:
                p.parent.left = p
            else:
                p.parent.right = p
        q.update()
        return p

    def __str__(self):
        lines, *_ = self.__display_aux()
        return '\n'.join(lines)

    def __display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if not self.right and not self.left:
            line = f"{self.val}({self.height})({self.size})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if not self.right:
            lines, n, p, x = self.left.__display_aux()
            s = f"{self.val}({self.height})({self.size})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if not self.left:
            lines, n, p, x = self.right.__display_aux()
            s = f"{self.val}({self.height})({self.size})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.__display_aux()
        right, m, q, y = self.right.__display_aux()
        s = f"{self.val}({self.height})({self.size})"
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


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.node = Node(nums[0]) if nums else None
        for num in nums[1:]:
            self.node = self.node.add(num)

    def add(self, val: int) -> int:
        if not self.node:
            self.node = Node(val)
        else:
            self.node = self.node.add(val)
        return self.node.get(self.k)


def main():
    nums = list(reversed(range(16)))
    k = 3
    solution = KthLargest(k, nums)
    print(solution.node)
    print(solution.add(3))
    print(solution.node)
    print(solution.add(5))
    print(solution.node)
    print(solution.add(10))
    print(solution.node)
    print(solution.add(9))
    print(solution.node)
    print(solution.add(20))
    print(solution.node)


if __name__ == '__main__':
    main()

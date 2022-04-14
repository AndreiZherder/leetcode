"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 2^31 - 1
"""
from typing import List, Optional


class Node:
    def __init__(self, val: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
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
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Node(-1)
        for num in nums:
            node = root
            mask = 0x40000000
            while mask:
                if num & mask:
                    if not node.right:
                        node.right = Node(mask)
                    node = node.right
                else:
                    if not node.left:
                        node.left = Node(0)
                    node = node.left
                mask >>= 1
        maximum = 0
        for num in nums:
            current = 0
            node = root
            mask = 0x40000000
            while mask:
                if num & mask:
                    if node.left:
                        current += mask
                        node = node.left
                    else:
                        node = node.right
                else:
                    if node.right:
                        current += mask
                        node = node.right
                    else:
                        node = node.left
                mask >>= 1
            maximum = max(maximum, current)
        return maximum


def main():
    print(Solution().findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))


if __name__ == '__main__':
    main()

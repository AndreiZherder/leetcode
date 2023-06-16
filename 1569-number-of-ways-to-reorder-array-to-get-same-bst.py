"""
YGiven an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.



Example 1:
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST:
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


mod = 10 ** 9 + 7


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Given two integers a and b, returns (gcd(a, b), x, y) such that
    a * x + b * y == gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def mmul(x: int, y: int) -> int:
    return (x * y) % mod


def minv(x: int) -> int:
    """
    returns modular inverse of x when mod is prime or not prime
    ans = (1 / x) % mod
    gcd(y, mod) should be 1
    """
    g, inv, _ = egcd(x, mod)
    if g != 1:
        raise ValueError('gcd(x, mod) != 1')
    return inv % mod


def mdiv(x: int, y: int) -> int:
    """
    returns (x / y) % mod
    gcd(y, mod) should be 1
    """
    return (x * minv(y)) % mod


def ncr(n: int, r: int) -> int:
    """
    returns number of ways for selecting r elements out of n options
    """
    num, den = 1, 1
    for i in range(r):
        num = mmul(num, n - i)
        den = mmul(den, i + 1)
    return mdiv(num, den)


def add(root: TreeNode, num: int):
    if num < root.val:
        if not root.left:
            root.left = TreeNode(num)
        else:
            add(root.left, num)
    else:
        if not root.right:
            root.right = TreeNode(num)
        else:
            add(root.right, num)


def dp(root: TreeNode) -> Tuple[int, int]:
    if not root:
        return 1, 0
    x, n = dp(root.left)
    y, m = dp(root.right)
    return (((x * y) % mod) * ncr(n + m, min(n, m))) % mod, n + m + 1


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        root = TreeNode(nums[0])
        for num in nums[1:]:
            add(root, num)
        return dp(root)[0] - 1


def main():
    nums = [3, 4, 5, 1, 2]
    print(Solution().numOfWays(nums))


if __name__ == '__main__':
    main()

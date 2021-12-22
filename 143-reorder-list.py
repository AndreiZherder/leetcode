"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        n = len(nodes)
        curr = head
        for i in range(n - 1, n // 2, -1):
            nodes[i].next = curr.next
            curr.next = nodes[i]
            curr = nodes[i].next
            nodes[i - 1].next = None


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    dummy = ListNode(0)
    node, prev = dummy, dummy
    for num in lst:
        node = ListNode(num)
        prev.next = node
        prev = node
    head = dummy.next
    Solution().reorderList(head)
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next


if __name__ == '__main__':
    main()

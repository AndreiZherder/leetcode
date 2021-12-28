"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


def main():
    solution = Solution()
    node = None
    prev_node = None
    for num in reversed([-1, 5, 3, 4, 0, 8, 3, 2, 1]):
        node = ListNode(num, prev_node)
        prev_node = node
    head = node
    head = solution.middleNode(head)
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next


if __name__ == '__main__':
    main()

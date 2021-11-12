"""
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


Constraints:

The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= val <= 50
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addElements(self, head: Optional[ListNode], vals: list) -> Optional[ListNode]:
        node = head
        if node:
            while node.next:
                node = node.next
        for val in vals:
            if not node:
                node = ListNode(val)
                head = node
            else:
                new = ListNode(val)
                node.next = new
                node = node.next
        return head

    def printElements(self, head: Optional[ListNode]):
        node = head
        if node:
            while node.next:
                print(node.val, end=' ')
                node = node.next
            print(node.val, end=' ')
            print()

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        if head.val == val:
            if head.next:
                head = head.next
            else:
                head = None
        return head


elements = [1, 2, 6, 3, 4, 5, 6]
solution = Solution()
head: Optional[ListNode] = None
head = solution.addElements(head, elements)
solution.printElements(head)
head = solution.removeElements(head, 6)
solution.printElements(head)

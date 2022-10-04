"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for i in range(1, n):
            first = first.next
        dummy = ListNode(0, head)
        second = dummy
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


def make_list(array: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    node = dummy
    for num in array:
        node.next = ListNode(num)
        node = node.next
    return dummy.next


def print_list(head: ListNode):
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


def main():
    head = [1, 2, 3, 4, 5]
    n = 2
    head = make_list(head)
    print_list(head)
    print_list(Solution().removeNthFromEnd(head, n))


if __name__ == '__main__':
    main()

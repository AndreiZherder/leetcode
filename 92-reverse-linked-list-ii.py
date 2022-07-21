"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        node1 = ListNode(next=head)
        dummy = node1
        for i in range(left - 1):
            node1 = node1.next
        first = node1.next
        curr = first.next
        prev = first
        for i in range(right - left):
            curr.next, curr, prev = prev, curr.next, curr
        node1.next = prev
        first.next = curr
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
    list1 = [1, 2, 3, 4, 5, 6]
    head = make_list(list1)
    print_list(head)
    print_list(Solution().reverseBetween(head, 1, 6))


if __name__ == '__main__':
    main()

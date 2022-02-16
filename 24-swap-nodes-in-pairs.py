"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if not first:
            return head
        second = first.next
        if second:
            if second.next:
                if second.next.next:
                    first.next = second.next.next
                else:
                    first.next = second.next
            else:
                first.next = None
            third = second.next
            second.next = first
            head = second
        else:
            return head

        first = third
        while first:
            if not first:
                return head
            second = first.next
            if second:
                if second.next:
                    if second.next.next:
                        first.next = second.next.next
                    else:
                        first.next = second.next
                else:
                    first.next = None
                third = second.next
                second.next = first
            else:
                return head
            first = third

        return head


def make_list(array: List[int]) -> Optional[ListNode]:
    if not array:
        return
    head = ListNode(array[0])
    tail = head
    for num in array[1:]:
        tail.next = ListNode(num)
        tail = tail.next
    return head


def print_list(head: ListNode):
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


def main():
    array = [1, 2, 3, 4, 5, 6]
    head = make_list(array)
    print_list(head)
    head = Solution().swapPairs(head)
    print_list(head)


if __name__ == '__main__':
    main()

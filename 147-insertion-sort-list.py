"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data,
finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = head
        node = head.next
        while node:
            if node.val < prev_node.val:
                prev_node.next = node.next
                if node.val < head.val:
                    node.next = head
                    head = node
                else:
                    prev_node2 = head
                    node2 = head.next
                    while node2.val < node.val:
                        node2 = node2.next
                        prev_node2 = prev_node2.next
                    node.next = node2
                    prev_node2.next = node
                node = prev_node.next
            else:
                node = node.next
                prev_node = prev_node.next
        return head


def main():
    solution = Solution()
    node = None
    prev_node = None
    for num in reversed([-1, 5, 3, 4, 0]):
        node = ListNode(num, prev_node)
        prev_node = node
    head = node
    head = solution.insertionSortList(head)
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next


if __name__ == '__main__':
    main()

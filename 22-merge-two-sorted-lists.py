"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.val <= node2.val:
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next
        node = head
        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node = node.next
                node1 = node1.next
            else:
                node.next = node2
                node = node.next
                node2 = node2.next
        if node1:
                node.next = node1
        if node2:
                node.next = node2
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
    arrays = [[1, 2, 4], [1, 3, 4]]
    lists = [make_list(array) for array in arrays]
    for list in lists:
        print_list(list)
    head = Solution().mergeTwoLists(lists[0], lists[1])
    print_list(head)


if __name__ == '__main__':
    main()

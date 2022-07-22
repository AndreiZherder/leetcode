"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        node1 = dummy1
        node2 = dummy2
        node = head
        while node:
            if node.val < x:
                node1.next = node
                node1 = node1.next
            else:
                node2.next = node
                node2 = node2.next
            node = node.next
        node2.next = None
        node1.next = dummy2.next
        return dummy1.next


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
    list1 = [3, 2]
    x = 3
    head = make_list(list1)
    print_list(head)
    print_list(Solution().partition(head,x))


if __name__ == '__main__':
    main()

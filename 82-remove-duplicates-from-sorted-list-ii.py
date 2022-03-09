"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(101, head)
        prev = dummy
        node = head
        while node:
            if node.next and node.next.val == node.val:
                while node.next and node.next.val == node.val:
                    node = node.next
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy.next


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
    array = [1, 1, 1, 2, 3, 3, 3, 3, 5, 6, 6, 6]
    head = make_list(array)
    print_list(head)
    head = Solution().deleteDuplicates(head)
    print_list(head)


if __name__ == '__main__':
    main()

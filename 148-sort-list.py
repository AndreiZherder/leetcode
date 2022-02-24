"""
Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-10^5 <= Node.val <= 10^5


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


"""
from heapq import heappush, heappop
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        heap = []
        while node:
            heappush(heap, (node.val, id(node), node))
            node = node.next

        head = heappop(heap)[2]
        tail = head
        while heap:
            tail.next = heappop(heap)[2]
            tail = tail.next
        tail.next = None
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
    array = [4, 19, 14, 5, -3, 1, 8, 5, 11, 15]
    head = make_list(array)
    print_list(head)
    head = Solution().sortList(head)
    print_list(head)


if __name__ == '__main__':
    main()

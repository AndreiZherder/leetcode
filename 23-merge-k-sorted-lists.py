"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
from functools import total_ordering
from heapq import heappush, heappop
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@total_ordering
class AbleToOrderNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __eq__(self, other):
        return self.node.val == other.node.val

    def __le__(self, other):
        return self.node.val <= other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        head = None
        tail = head
        for node in lists:
            if node:
                heappush(q, AbleToOrderNode(node))
        if q:
            head = heappop(q).node
            tail = head
            if tail.next:
                heappush(q, AbleToOrderNode(tail.next))
        while q:
            tail.next = heappop(q).node
            tail = tail.next
            if tail.next:
                heappush(q, AbleToOrderNode(tail.next))
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
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [make_list(array) for array in arrays]
    for list in lists:
        print_list(list)
    head = Solution().mergeKLists(lists)
    print_list(head)


if __name__ == '__main__':
    main()

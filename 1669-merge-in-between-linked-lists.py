"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:
Build the result list and return its head.



Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place.
The blue edges and nodes in the above figure indicate the result.
Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.


Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = None
        end = None
        dummy = ListNode(0, list1)
        node = dummy
        for i in range(a):
            node = node.next
        start = node
        for i in range(b - a + 1):
            node = node.next
        end = node.next

        start.next = list2
        node = list2
        while node.next:
            node = node.next
        node.next = end

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
    list1 = [10, 1, 13, 6, 9, 5]
    a = 3
    b = 4
    list2 = [1000000, 1000001, 1000002]
    head1 = make_list(list1)
    print_list(head1)
    head2 = make_list(list2)
    print_list(head2)
    head = Solution().mergeInBetween(head1, a, b, head2)
    print_list(head)


if __name__ == '__main__':
    main()

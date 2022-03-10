"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        node = dummy
        while node1 and node2:
            val = node1.val + node2.val + carry
            carry = val // 10
            node.next = ListNode(val % 10)
            node = node.next
            node1 = node1.next
            node2 = node2.next
        while node1:
            val = node1.val + carry
            carry = val // 10
            if carry == 0:
                node.next = ListNode(val % 10)
                node = node.next
                node.next = node1.next
                break
            node.next = ListNode(val % 10)
            node = node.next
            node1 = node1.next
        while node2:
            val = node2.val + carry
            carry = val // 10
            if carry == 0:
                node.next = ListNode(val % 10)
                node = node.next
                node.next = node2.next
                break
            node.next = ListNode(val % 10)
            node = node.next
            node2 = node2.next
        if carry:
            node.next = ListNode(carry)
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
    list1 = [9, 9, 9, 9, 9, 9, 9]
    head1 = make_list(list1)
    list2 = [9, 9, 9, 9]
    head2 = make_list(list2)
    print_list(head1)
    print_list(head2)
    head = Solution().addTwoNumbers(head1, head2)
    print_list(head)


if __name__ == '__main__':
    main()

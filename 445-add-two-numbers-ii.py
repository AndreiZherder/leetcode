"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


Follow up: Could you solve it without reversing the input lists?
"""
from itertools import zip_longest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def read(head: ListNode) -> List[int]:
            node = head
            ans = []
            while node:
                ans.append(node.val)
                node = node.next
            return ans

        a = read(l1)
        b = read(l2)
        carry = 0
        head = None
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue=0):
            cur = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            head = ListNode(cur, head)
        if carry:
            head = ListNode(1, head)
        return head



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

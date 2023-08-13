"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.



Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189.
Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999.
Hence, the returned linked list reprersents the number 999 * 2 = 1998.


Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros,
except the number 0 itself.

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        n = len(arr)
        double = []
        carry = 0
        for num in reversed(arr):
            double.append(num * 2 % 10 + carry)
            carry = num * 2 // 10
        if carry:
            double.append(carry)
        dummy = ListNode(-1)
        node = dummy
        for num in reversed(double):
            node.next = ListNode(num)
            node = node.next
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
    list1 = [9, 9, 9]
    head1 = make_list(list1)
    print_list(head1)
    head = Solution().doubleIt(head1)
    print_list(head)


if __name__ == '__main__':
    main()

"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        node = head
        tail = node
        n = 0
        while node:
            tail = node
            node = node.next
            n += 1
        k = k % n
        if k == 0:
            return head
        node = head
        for i in range(n - k - 1):
            node = node.next
        tail.next = head
        head = node.next
        node.next = None
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
    list1 = [1, 2, 3, 4, 5]
    head = make_list(list1)
    print_list(head)
    head = Solution().rotateRight(head, 7)
    print_list(head)


if __name__ == '__main__':
    main()

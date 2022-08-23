"""
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, prev = prev, slow.next, slow
        if fast:
            slow = slow.next
        while slow:
            if slow.val != prev.val:
                return False
            else:
                slow, prev = slow.next, prev.next
        return True



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
    list1 = [1, 2, 3, 2, 1]
    head = make_list(list1)
    print_list(head)
    print(Solution().isPalindrome(head))


if __name__ == '__main__':
    main()

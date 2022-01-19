"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
Note that pos is not passed as a parameter.

Do not modify the linked list.



Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
https://stackoverflow.com/questions/2936213/how-does-finding-a-cycle-start-node-in-a-cycle-linked-list-work
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast = head
        slow = head
        met = 0
        while fast.next and fast.next.next:
            fast = fast.next.next if not met else fast.next
            slow = slow.next
            if fast == slow:
                if not met:
                    if slow == head:
                        return head
                    slow = head
                    met = 1
                else:
                    return slow


def main():
    lst = [1, 2]
    head = ListNode(lst[0]) if lst else None
    node = head
    for num in lst[1:]:
        node.next = ListNode(num)
        node = node.next
    node.next = head

    print(Solution().detectCycle(head))


if __name__ == '__main__':
    main()

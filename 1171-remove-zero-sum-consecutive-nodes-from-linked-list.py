"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are
no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]


Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        n = len(nums)
        pref = [0 for i in range(n)]
        d = {0: -1}
        stack = []
        for i, num in enumerate(nums):
            pref[i] = pref[i - 1] + num
            if pref[i] in d:
                j = d[pref[i]]
                while stack and stack[-1] > j:
                    del d[pref[stack[-1]]]
                    stack.pop()
            else:
                d[pref[i]] = i
                stack.append(i)

        dummy = ListNode(0)
        node = dummy
        for i in stack:
            node.next = ListNode(nums[i])
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
    list1 = [1, 2, -3, 3, 1]
    head1 = make_list(list1)
    print_list(head1)
    head = Solution().removeZeroSumSublists(head1)
    print_list(head)


if __name__ == '__main__':
    main()

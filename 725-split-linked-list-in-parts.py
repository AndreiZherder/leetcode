"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one.
This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always
have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.


Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50

"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        m, rem = divmod(n, k)
        ans = []
        node = head
        first = node
        for i in range(rem):
            for j in range(m):
                node = node.next
            if node:
                tmp = node.next
                node.next = None
                node = tmp
            ans.append(first)
            first = node
        for i in range(k - rem):
            for j in range(m - 1):
                node = node.next
            if node:
                tmp = node.next
                node.next = None
                node = tmp
            ans.append(first)
            first = node
        return ans


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
    list1 = [1, 2, 3]
    k = 5
    head = make_list(list1)
    print_list(head)
    print(Solution().splitListToParts(head, k))


if __name__ == '__main__':
    main()

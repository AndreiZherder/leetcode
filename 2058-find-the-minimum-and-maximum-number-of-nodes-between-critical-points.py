"""
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance
is the minimum distance between any two distinct critical points and maxDistance is
the maximum distance between any two distinct critical points. If there are fewer than two critical points,
return [-1, -1].



Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].
Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
Example 3:
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.


Constraints:

The number of nodes in the list is in the range [2, 105].
1 <= Node.val <= 105
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        node = head.next
        prev = head.val
        a = []
        i = 1
        while node.next:
            if prev < node.val > node.next.val or prev > node.val < node.next.val:
                a.append(i)
            i += 1
            prev = node.val
            node = node.next
        if len(a) < 2:
            return [-1, -1]
        else:
            mn = 10 ** 20
            for x, y in zip(a, a[1:]):
                mn = min(mn, y - x)
        return [mn, a[-1] - a[0]]


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
    list1 = [1, 3, 2, 2, 3, 2, 2, 2, 7]
    head1 = make_list(list1)
    print_list(head1)
    print(Solution().nodesBetweenCriticalPoints(head1))


if __name__ == '__main__':
    main()

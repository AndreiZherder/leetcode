"""
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Constraints:

0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.

"""
from typing import Optional, List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(0)
        node = head
        node1 = Node(node.val)
        copied = {node: node1}
        dummy.next = node1
        while node:
            if node.next:
                if node.next in copied:
                    node1.next = copied[node.next]
                else:
                    node1.next = Node(node.next.val)
                    copied[node.next] = node1.next
            else:
                node1.next = None
            if node.random:
                if node.random in copied:
                    node1.random = copied[node.random]
                else:
                    node1.random = Node(node.random.val)
                    copied[node.random] = node1.random
            else:
                node1.random = None
            node = node.next
            node1 = node1.next
        return dummy.next


def make_list(array: List[int]) -> Optional[Node]:
    dummy = Node(0)
    node = dummy
    for num in array:
        node.next = Node(num)
        node = node.next
    return dummy.next


def print_list(head: Node):
    node = head
    while node:
        print(f'{node.val}[{node.random.val if node.random else None}]', end=' ')
        node = node.next
    print()


def main():
    list1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = make_list([pair[0] for pair in list1])
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    for i in range(len(nodes)):
        nodes[i].random = nodes[list1[i][1]] if list1[i][1] is not None else None
    print_list(head)
    head1 = Solution().copyRandomList(head)
    print_list(head1)


if __name__ == '__main__':
    main()

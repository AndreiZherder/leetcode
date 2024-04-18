"""
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise),
starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.



Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.


Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000

"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def coords(a: List[List[int]]) -> (int, int):
            i = 0
            j = 0
            while True:
                while j < m and a[i][j] == -1:
                    yield i, j
                    j += 1
                i += 1
                j -= 1
                while i < n and a[i][j] == -1:
                    yield i, j
                    i += 1
                i -= 1
                j -= 1
                while j > -1 and a[i][j] == -1:
                    yield i, j
                    j -= 1
                i -= 1
                j += 1
                while a[i][j] == -1:
                    yield i, j
                    i -= 1
                i += 1
                j += 1

        n, m = m, n
        a = [[-1 for j in range(m)] for i in range(n)]
        node = head
        gen = coords(a)
        for k in range(n * m):
            i, j = next(gen)
            if node:
                a[i][j] = node.val
                node = node.next
            else:
                break
        return a


def main():
    m = 3
    n = 5
    list1 = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    head1 = make_list(list1)
    print(Solution().spiralMatrix(m, n, head1))


if __name__ == '__main__':
    main()

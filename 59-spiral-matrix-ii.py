"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a = [[0 for j in range(n)] for i in range(n)]
        gen = self.coords(a)
        for k in range(n * n):
            i, j = next(gen)
            a[i][j] = k + 1
        return a

    def coords(self, a: List[List[int]]) -> (int, int):
        n = len(a)
        i = 0
        j = 0
        while True:
            while j < n and a[i][j] == 0:
                yield i, j
                j += 1
            i += 1
            j -= 1
            while i < n and a[i][j] == 0:
                yield i, j
                i += 1
            i -= 1
            j -= 1
            while j > -1 and a[i][j] == 0:
                yield i, j
                j -= 1
            i -= 1
            j += 1
            while a[i][j] == 0:
                yield i, j
                i -= 1
            i += 1
            j += 1


def main():
    print(*Solution().generateMatrix(5), sep='\n')


if __name__ == '__main__':
    main()

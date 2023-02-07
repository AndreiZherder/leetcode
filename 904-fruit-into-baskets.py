"""
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Constraints:

1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
"""
from collections import deque
from itertools import chain
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        q = deque([-2, fruits[0]], maxlen=2)
        start_so_far = 0
        cur_start = 0
        best = 0
        for i, fruit in enumerate(chain(fruits[1:], [-1]), start=1):
            if fruit not in q:
                best = max(best, i - start_so_far)
                q.append(fruit)
                start_so_far = cur_start
                cur_start = i
            elif fruit == q[0]:
                cur_start = i
                q.rotate(1)
        return best


def main():
    fruits = [1, 2, 3, 2, 2]
    print(Solution().totalFruit(fruits))


if __name__ == '__main__':
    main()

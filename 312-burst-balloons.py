"""
You are given n balloons, indexed from 0 to n - 1.
Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10


Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""
from copy import deepcopy
from itertools import permutations
from typing import List


class Node:
    def __init__(self, val: int, prev: int, next: int):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nodes = [Node(1, -1, 1)] + \
                [Node(num, i, i + 2) for i, num in enumerate(nums)] + \
                [Node(1, len(nums), len(nums) + 2)]
        ans = []
        for seq in permutations(range(1, len(nums) + 1), len(nums)):
            ans.append([self.coins(deepcopy(nodes), seq), seq])
        coins, seq = max(ans, key=lambda x: x[0])
        print(coins, seq, [nodes[i].val for i in seq])
        for i in seq:
            j = nodes[0].next
            while j != len(seq) + 1:
                print(nodes[j].val, end=' ')
                j = nodes[j].next
            print()
            j = nodes[0].next
            while j != len(seq) + 1:
                print(nodes[nodes[j].prev].val * nodes[j].val * nodes[nodes[j].next].val, end=' ')
                j = nodes[j].next
            print()
            nodes[nodes[i].prev].next = nodes[i].next
            nodes[nodes[i].next].prev = nodes[i].prev
        return 0

    def coins(self, nodes: List['Node'], seq: List[int]) -> int:
        ans = 0
        for i in seq:
            ans += nodes[nodes[i].prev].val * nodes[i].val * nodes[nodes[i].next].val
            nodes[nodes[i].prev].next = nodes[i].next
            nodes[nodes[i].next].prev = nodes[i].prev
        return ans


def main():
    numss = [[7, 3, 5, 9, 3, 2, 12],
             [7, 3, 5, 9, 3, 2, 25],
             ]
    solution = Solution()
    for nums in numss:
        solution.maxCoins(nums)
    # print(Solution().maxCoins(nums))


if __name__ == '__main__':
    main()

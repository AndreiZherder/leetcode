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
from heapq import heappush, heappop
from itertools import permutations
from typing import List


class Node:
    def __init__(self, val: int, prev: int, next: int):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def bruteforce(self, nums: List[int]) -> int:
        nodes = [Node(1, -1, 1)] + [Node(1, 0, 2)] + \
                [Node(num, i + 1, i + 3) for i, num in enumerate(nums)] + \
                [Node(1, len(nums) + 1, len(nums) + 3)] + [Node(1, len(nums) + 2, len(nums) + 4)]
        ans = []
        for seq in permutations(range(2, len(nums) + 2), len(nums)):
            ans.append([self.coins(deepcopy(nodes), seq), seq])
        coins, seq = max(ans, key=lambda x: x[0])
        print(coins, seq, [nodes[i].val for i in seq])
        for i in seq:
            j = nodes[1].next
            while j != len(seq) + 2:
                print(nodes[j].val, end=' ')
                j = nodes[j].next
            print()
            j = nodes[1].next
            while j != len(seq) + 2:
                print(self.get_cost(nodes, j), end=' ')
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

    def maxCoins_first_version(self, nums: List[int]) -> int:
        ans = 0
        nodes = [Node(1, -1, 1)] + [Node(1, 0, 2)] + \
                [Node(num, i + 1, i + 3) for i, num in enumerate(nums)] + \
                [Node(1, len(nums) + 1, len(nums) + 3)] + [Node(1, len(nums) + 2, len(nums) + 4)]
        n = len(nums)
        while n > 0:
            i = nodes[1].next
            maximum_i = i
            maximum = -float('Inf')
            while i != len(nums) + 2:
                tmp = self.get_cost(nodes, i)
                if tmp > maximum:
                    maximum = tmp
                    maximum_i = i
                i = nodes[i].next
            ans += nodes[nodes[maximum_i].prev].val * nodes[maximum_i].val * nodes[nodes[maximum_i].next].val
            nodes[nodes[maximum_i].prev].next = nodes[maximum_i].next
            nodes[nodes[maximum_i].next].prev = nodes[maximum_i].prev
            n -= 1
        return ans

    def get_cost(self, nodes: List['Node'], i: int) -> int:
        return nodes[nodes[i].prev].val * nodes[nodes[i].next].val * \
               (nodes[i].val +
                nodes[nodes[nodes[i].prev].prev].val +
                nodes[nodes[nodes[i].next].next].val)

    def maxCoins(self, nums: List[int]) -> int:
        ans = 0
        nodes = [Node(1, -1, 1)] + [Node(1, 0, 2)] + \
                [Node(num, i + 1, i + 3) for i, num in enumerate(nums)] + \
                [Node(1, len(nums) + 1, len(nums) + 3)] + [Node(1, len(nums) + 2, len(nums) + 4)]
        n = len(nums)
        queue = []
        node_ids = {}
        cnt = 0
        i = nodes[1].next
        while i != len(nums) + 2:
            cost = self.get_cost(nodes, i)
            heappush(queue, (-cost, i, cnt))
            node_ids[i] = cnt
            cnt += 1
            i = nodes[i].next

        while n > 0:
            cost, i, node_id = heappop(queue)
            if node_id == node_ids[i]:
                ans += nodes[nodes[i].prev].val * nodes[i].val * nodes[nodes[i].next].val

                nodes[nodes[i].prev].next = nodes[i].next
                nodes[nodes[i].next].prev = nodes[i].prev

                i = nodes[i].prev
                i = nodes[i].prev
                if i > 1:
                    cost = self.get_cost(nodes, i)
                    heappush(queue, (-cost, i, cnt))
                    node_ids[i] = cnt
                    cnt += 1

                i = nodes[i].next
                if i > 1:
                    cost = self.get_cost(nodes, i)
                    heappush(queue, (-cost, i, cnt))
                    node_ids[i] = cnt
                    cnt += 1

                i = nodes[i].next
                if i < len(nums) + 2:
                    cost = self.get_cost(nodes, i)
                    heappush(queue, (-cost, i, cnt))
                    node_ids[i] = cnt
                    cnt += 1

                i = nodes[i].next
                if i < len(nums) + 2:
                    cost = self.get_cost(nodes, i)
                    heappush(queue, (-cost, i, cnt))
                    node_ids[i] = cnt
                    cnt += 1
                n -= 1
        return ans


def main():
    lists = [[7, 3, 5, 9, 3, 2, 12],
             [7, 3, 5, 9, 3, 2, 25],
             [3, 1, 5, 8],
             [35, 16, 83, 87, 84, 59, 48, 41]
             ]
    solution = Solution()
    for nums in lists:
        solution.bruteforce(nums)
    for nums in lists:
        print(solution.maxCoins_first_version(nums))
    for nums in lists:
        print(solution.maxCoins(nums))


if __name__ == '__main__':
    main()

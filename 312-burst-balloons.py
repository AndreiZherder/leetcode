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
from functools import lru_cache
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

    def get_cost(self, nodes: List['Node'], i: int) -> int:
        return nodes[nodes[i].prev].val * nodes[nodes[i].next].val * \
               (nodes[i].val +
                nodes[nodes[nodes[i].prev].prev].val +
                nodes[nodes[nodes[i].next].next].val)

    def maxCoins_recursive(self, nums: List[int]) -> int:
        @lru_cache
        def helper(i: int, j: int) -> int:
            ans = 0
            if i <= j:
                for k in range(i, j + 1):
                    ans = max(ans, nums[i - 1] * nums[k] * nums[j + 1] + helper(i, k - 1) + helper(k + 1, j))
            return ans

        nums = [1] + nums + [1]
        return helper(1, len(nums) - 2)

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        for length in range(1, n - 1):
            for i in range(1, n - length):
                j = i + length - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j])
        return dp[1][n - 2]


def main():
    lists = [[7, 3, 5, 9, 3, 2, 12],
             [7, 3, 5, 9, 3, 2, 25],
             [3, 1, 5, 8],
             [35, 16, 83, 87, 84, 59, 48, 41],
             [4, 1, 4, 9, 4, 1, 8, 1, 8, 6, 9, 1, 2, 0, 9, 6, 4, 1, 7, 9, 5, 4, 4, 0]
             ]
    solution = Solution()
    # for nums in lists:
    #     solution.bruteforce(nums)
    #     print()
    for nums in lists:
        print(solution.maxCoins(nums))


if __name__ == '__main__':
    main()

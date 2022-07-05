"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Node:
    def __init__(self, parent: int, val: int, rank: int = 0, size: int = 1):
        self.parent = parent
        self.rank = rank
        self.size = size
        self.val = val


class DSU:
    def __init__(self, nums: List[int]):
        self.nodes = [Node(i, nums[i]) for i in range(len(nums))]
        self.max_size = 1

    def find(self, i: int) -> int:
        while i != self.nodes[i].parent:
            i = self.nodes[i].parent
        return i

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.nodes[id1].rank > self.nodes[id2].rank:
            self.nodes[id2].parent = id1
            self.nodes[id1].size += self.nodes[id2].size
            self.max_size = max(self.max_size, self.nodes[id1].size)
        else:
            self.nodes[id1].parent = id2
            self.nodes[id2].size += self.nodes[id1].size
            self.max_size = max(self.max_size, self.nodes[id2].size)
            if self.nodes[id1].rank == self.nodes[id2].rank:
                self.nodes[id2].rank += 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = dict()
        dsu = DSU(nums)
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
                if num - 1 in d:
                    dsu.union(i, d[num - 1])
                if num + 1 in d:
                    dsu.union(i, d[num + 1])
        return dsu.max_size


def main():
    # nums = [100, 4, 200, 1, 3, 2]
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums = [1, 2, 0, 1]
    print(Solution().longestConsecutive(nums))


if __name__ == '__main__':
    main()

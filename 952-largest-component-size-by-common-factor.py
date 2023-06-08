"""
You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.



Example 1:
Input: nums = [4,6,15,35]
Output: 4
Example 2:
Input: nums = [20,50,9,63]
Output: 2
Example 3:
Input: nums = [2,3,6,7,4,12,21,39]
Output: 8


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 105
All the values of nums are unique.

"""
from collections import defaultdict, Counter
from typing import List


def prime_factors(n: int):
    """
    Prime factors of n
    prime_factors(99) --> 3 3 11
    """
    while n % 2 == 0:
        yield 2
        n //= 2
    p = 3
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            n = quotient
        else:
            p += 2
    if n != 1:
        yield n


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        dsu = DSU(n)
        d = defaultdict(list)
        for i, num in enumerate(nums):
            for p in prime_factors(num):
                d[p].append(i)
        for indexes in d.values():
            for j in range(1, len(indexes)):
                dsu.union(indexes[j], indexes[j - 1])
        return max(Counter(dsu.find(i) for i in range(n)).values())


def main():
    nums = [2, 3, 6, 7, 4, 12, 21, 39]
    print(Solution().largestComponentSize(nums))


if __name__ == '__main__':
    main()

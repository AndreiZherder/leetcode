"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times.
Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.



Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 10^9
All the values of arr are unique.
"""
from functools import reduce
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        maximum = arr[-1]
        tree = {num: [] for num in arr}
        for factor1 in tree:
            for factor2 in tree:
                product = factor1 * factor2
                if product > maximum:
                    break
                if product in tree:
                    tree[product].append((factor1, factor2))
        count = {num: 1 for num in arr}
        for product in count:
            acc = 0
            for factor1, factor2 in tree[product]:
                acc = (acc + count[factor1] * count[factor2] % mod) % mod
            count[product] += acc
        return reduce(lambda x, y: (x + y) % mod, count.values())


def main():
    arr = [2, 4, 8]
    print(Solution().numFactoredBinaryTrees(arr))


if __name__ == '__main__':
    main()

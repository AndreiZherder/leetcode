"""
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""
from functools import reduce
from itertools import groupby, accumulate
from operator import mul
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if 0 in nums:
            best = 0
        else:
            best = -10 ** 20
        arrs = [list(group) for k, group in groupby(nums, lambda x: x == 0) if not k]
        for arr in arrs:
            if len(arr) == 1:
                best = max(best, arr[0])
            elif sum(num < 0 for num in arr) % 2 == 0:
                best = max(best, reduce(mul, arr))
            else:
                product = reduce(mul, arr)
                pref = list(accumulate(arr, mul))
                for i, num in enumerate(arr):
                    if num < 0:
                        if i != 0:
                            best = max(best, pref[i - 1])
                        if i != len(arr) - 1:
                            best = max(best, product // pref[i])
        return best


def main():
    nums = [2, 3, -2, 4]
    print(Solution().maxProduct(nums))


if __name__ == '__main__':
    main()

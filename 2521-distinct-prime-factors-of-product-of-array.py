"""
Given an array of positive integers nums, return the number of distinct prime factors in the product
of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.


Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.
Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.


Constraints:

1 <= nums.length <= 10^4
2 <= nums[i] <= 1000
"""
import math
from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        def sieve(n: int):
            nums = [True for i in range(n + 1)]
            p = 2
            while p * p < n + 1:
                if nums[p]:
                    for i in range(p * p, n + 1, p):
                        nums[i] = False
                p += 1
            for p in range(2, n + 1):
                if nums[p]:
                    yield p

        def factors(n):
            """
            Prime factors of n.
            # factor(99) --> 3 3 11
            """
            for prime in sieve(math.isqrt(n) + 1):
                while n > 1:
                    quotient, remainder = divmod(n, prime)
                    if remainder:
                        break
                    yield prime
                    n = quotient
            if n > 1:
                yield n

        s = set()
        for num in nums:
            s.update(factors(num))
        return len(s)


def main():
    nums = [2, 4, 3, 7, 10, 6]
    print(Solution().distinctPrimeFactors(nums))


if __name__ == '__main__':
    main()

"""
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= nums1 < nums2 <= right .
nums1 and nums2 are both prime numbers.
nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions,
return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.



Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.


Constraints:

1 <= left <= right <= 10^6
"""
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def is_prime(n):
            if n < 2:
                return False
            if n < 4:
                return True
            if n % 2 == 0:
                return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

        best = 10 ** 20
        ans = [-1, -1]
        primes = filter(is_prime, range(left, right + 1))
        prev = next(primes, 0)
        for num in primes:
            if num - prev < best:
                ans = [prev, num]
                best = num - prev
                if best <= 2:
                    return ans
            prev = num
        return ans


def main():
    left = 10
    right = 19
    print(Solution().closestPrimes(left, right))


if __name__ == '__main__':
    main()

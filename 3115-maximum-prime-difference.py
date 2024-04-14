"""
You are given an integer array nums.

Return an integer that is the maximum distance between the indices of two (not necessarily different)
prime numbers in nums.



Example 1:

Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:

Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.



Constraints:

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
The input is generated such that the number of prime numbers in the nums is at least one.

"""
from typing import List


def is_prime(n: int):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    # all primes > 3 are of the form 6n ± 1
    p = 5
    while p * p <= n:
        if n % p == 0:
            return False
        if n % (p + 2) == 0:
            return False
        p += 6
    return True


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while i <= j and not is_prime(nums[i]):
            i += 1
        while i <= j and not is_prime(nums[j]):
            j -= 1
        return j - i


def main():
    nums = [4, 2, 9, 5, 3]
    print(Solution().maximumPrimeDifference(nums))


if __name__ == '__main__':
    main()

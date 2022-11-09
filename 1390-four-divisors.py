"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.



Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0


Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""
from math import sqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divisors(num: int) -> List[int]:
            cnt = 0
            ans = []
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    cnt += 1
                    if cnt > 1:
                        return []
                    if num // i != i:
                        ans = [i, num // i]
            return ans

        ans = 0
        for num in nums:
            divisors = get_divisors(num)
            if divisors:
                ans += 1 + num + sum(divisors)
        return ans


def main():
    nums = [21, 4, 7]
    print(Solution().sumFourDivisors(nums))


if __name__ == '__main__':
    main()

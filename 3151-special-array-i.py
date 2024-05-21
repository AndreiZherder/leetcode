"""
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.



Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.



Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        INF = 10 ** 20
        n = len(nums)
        pref = [0]
        for i in range(1, n):
            if (nums[i] & 1) ^ (nums[i - 1] & 1):
                pref.append(pref[-1])
            else:
                pref.append(pref[-1] + INF)
        return pref[n - 1] - pref[0] < INF


def main():
    nums = [4, 3, 1, 6]
    print(Solution().isArraySpecial(nums))


if __name__ == '__main__':
    main()

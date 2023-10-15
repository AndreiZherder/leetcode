"""
You are given a 0-indexed integer array nums having length n, an integer indexDifference,
and an integer valueDifference.

Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

abs(i - j) >= indexDifference, and
abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise.
If there are multiple choices for the two indices, return any of them.

Note: i and j may be equal.



Example 1:

Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
Output: [0,3]
Explanation: In this example, i = 0 and j = 3 can be selected.
abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
Hence, a valid answer is [0,3].
[3,0] is also a valid answer.
Example 2:

Input: nums = [2,1], indexDifference = 0, valueDifference = 0
Output: [0,0]
Explanation: In this example, i = 0 and j = 0 can be selected.
abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
Hence, a valid answer is [0,0].
Other valid answers are [0,1], [1,0], and [1,1].
Example 3:

Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
Output: [-1,-1]
Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
Hence, [-1,-1] is returned.


Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= 109
0 <= indexDifference <= 105
0 <= valueDifference <= 109
"""
from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_pref = [0 for i in range(n)]
        max_pref = [0 for i in range(n)]
        for i in range(1, n):
            if nums[i] < nums[min_pref[i - 1]]:
                min_pref[i] = i
            else:
                min_pref[i] = min_pref[i - 1]
            if nums[i] > nums[max_pref[i - 1]]:
                max_pref[i] = i
            else:
                max_pref[i] = max_pref[i - 1]
        for i in range(n - 1, indexDifference - 1, -1):
            if abs(nums[i] - nums[min_pref[i - indexDifference]]) >= valueDifference:
                return [i, min_pref[i - indexDifference]]
            if abs(nums[i] - nums[max_pref[i - indexDifference]]) >= valueDifference:
                return [i, max_pref[i - indexDifference]]
        return [-1, -1]


def main():
    nums = [5, 1, 4, 1]
    indexDifference = 2
    valueDifference = 4
    print(Solution().findIndices(nums, indexDifference, valueDifference))


if __name__ == '__main__':
    main()

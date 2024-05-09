"""
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.



Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations.
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1]
which violates the conditions of an alternating array.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105

"""
from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums[::2])
        m = len(nums[1::2])
        c1 = sorted(Counter(nums[::2]).items(), key=lambda x: x[1], reverse=True)
        c2 = sorted(Counter(nums[1::2]).items(), key=lambda x: x[1], reverse=True)
        ans = 0
        if c1[0][0] != c2[0][0]:
            ans += n - c1[0][1]
            ans += m - c2[0][1]
        else:
            x1 = c1[1][1] if len(c1) > 1 else 0
            x2 = c2[1][1] if len(c2) > 1 else 0
            ans1 = n - c1[0][1] + m - x2
            ans2 = n - x1 + m - c2[0][1]
            ans = min(ans1, ans2)
        return ans


def main():
    nums = [3, 1, 3, 2, 4, 3]
    print(Solution().minimumOperations(nums))


if __name__ == '__main__':
    main()

"""
You are given a
binary array
 nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any index i from the array and flip all the elements from index i to the end of the array.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1.



Example 1:

Input: nums = [0,1,1,0,1]

Output: 4

Explanation:
We can do the following operations:

Choose the index i = 1. The resulting array will be nums = [0,0,0,1,0].
Choose the index i = 0. The resulting array will be nums = [1,1,1,0,1].
Choose the index i = 4. The resulting array will be nums = [1,1,1,0,0].
Choose the index i = 3. The resulting array will be nums = [1,1,1,1,1].
Example 2:

Input: nums = [1,0,0,0]

Output: 1

Explanation:
We can do the following operation:

Choose the index i = 1. The resulting array will be nums = [1,1,1,1].


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 1

"""
from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = n
        q = deque()
        ans = 0
        for i in range(n):
            while q and q[0] < i:
                q.popleft()
            if (nums[i] + len(q)) % 2 == 0:
                ans += 1
                q.append(i + k - 1)
        return ans


def main():
    nums = [0, 1, 1, 0, 1]
    print(Solution().minOperations(nums))


if __name__ == '__main__':
    main()

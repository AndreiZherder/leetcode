"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one
number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

"""
from collections import Counter
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        arr = []
        for i in range(k):
            for num in nums[i]:
                arr.append((num, i))
        arr.sort()
        n = len(arr)
        d = Counter()
        j = 0
        best = arr[-1][0] - arr[0][0]
        ans = [arr[0][0], arr[-1][0]]
        for i in range(n):
            d[arr[i][1]] += 1
            while len(d) == k:
                if arr[i][0] - arr[j][0] < best:
                    best = arr[i][0] - arr[j][0]
                    ans = [arr[j][0], arr[i][0]]
                d[arr[j][1]] -= 1
                if d[arr[j][1]] == 0:
                    del d[arr[j][1]]
                j += 1
        return ans


def main():
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(Solution().smallestRange(nums))


if __name__ == '__main__':
    main()

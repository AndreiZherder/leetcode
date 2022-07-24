"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from collections import deque
from typing import List


class Item:
    def __init__(self, i: int, num: int, acc: int = 0):
        self.i = i
        self.num = num
        self.acc = acc


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left: List[Item], right: List[Item]) -> List[Item]:
            n = len(left)
            m = len(right)
            i = 0
            j = 0
            k = 0
            ans = []
            while i < n and j < m:
                if left[i].num <= right[j].num:
                    left[i].acc += k
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
                    k += 1
            if i == n:
                while j < m:
                    ans.append(right[j])
                    j += 1
            if j == m:
                while i < n:
                    left[i].acc += k
                    ans.append(left[i])
                    i += 1
            return ans

        n = len(nums)
        q = deque([Item(i, num)] for i, num in enumerate(nums))
        while len(q) > 1:
            if len(q) % 2 == 1:
                right = q.pop()
                left = q.pop()
                res = merge(left, right)
                q.append(res)
            for i in range(len(q) // 2):
                left = q.popleft()
                right = q.popleft()
                res = merge(left, right)
                q.append(res)
        items = q.pop()
        ans = [0 for i in range(n)]
        for item in items:
            ans[item.i] = item.acc
        return ans


def main():
    nums = [5, 2, 6, 1]
    print(Solution().countSmaller(nums))


if __name__ == '__main__':
    main()

"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        if k == 1:
            return [max(d.items(), key=lambda x: x[1])[0]]
        h = []
        it = iter(d.items())
        i = 0
        while i < k:
            x = next(it)
            heapq.heappush(h, (x[1], x[0]))
            i += 1
        while i < len(d):
            x = next(it)
            if x[1] > h[0][0]:
                heapq.heapreplace(h, (x[1], x[0]))
            i += 1
        return [x[1] for x in h]


def main():
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))


if __name__ == '__main__':
    main()

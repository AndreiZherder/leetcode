"""
You are given an array target of n integers. From a starting array arr consisting of n 1's,
you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.



Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1]
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true


Constraints:

n == target.length
1 <= n <= 5 * 10^4
1 <= target[i] <= 10^9
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return True if target[0] == 1 else False
        heap = []
        s = 0
        for num in target:
            s += num
            heappush(heap, -num)
        num = -heappop(heap)
        others_sum = s - num
        if num <= others_sum:
            return False
        if num % others_sum == 0:
            num = num - (num // others_sum - 1) * others_sum
        else:
            num = num - num // others_sum * others_sum
        while True:
            heappush(heap, -num)
            s = num + others_sum
            num = -heappop(heap)
            if num == 1:
                return True
            others_sum = s - num
            if num <= others_sum:
                return False
            if num % others_sum == 0:
                num = num - (num // others_sum - 1) * others_sum
            else:
                num = num - num // others_sum * others_sum


def main():
    # target = [9, 3, 5]
    # target = [8, 5]
    # target = [1, 1, 1, 2]
    # target = [4, 7, 13, 25]
    # target = [1, 10]
    # target = [3, 5, 33]
    # target = [1, 1000000000]
    # target = [2, 900000002]
    target = [1]
    print(Solution().isPossible(target))


if __name__ == '__main__':
    main()

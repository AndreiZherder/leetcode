"""
Given an integer array arr and a target value target, return the integer value such that when we change
all the integers larger than value in the given array to be equal to value,
the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.



Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361


Constraints:

1 <= arr.length <= 104
1 <= arr[i], target <= 105

"""
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def comp(ans: int) -> int:
            return abs(sum(ans if num >= ans else num for num in arr) - target)

        def bsr(left: int, right: int) -> int:
            """
            TTTTFFFF
                |
            """

            def check(mid: int) -> bool:
                return sum(mid if num >= mid else num for num in arr) <= target

            while left <= right:
                mid = left + (right - left) // 2
                if check(mid):
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        arr.sort()
        ans = bsr(0, arr[-1]) - 1
        return min(ans, ans + 1, key=comp)


def main():
    arr = [60864, 25176, 27249, 21296, 20204]
    target = 56803
    print(Solution().findBestValue(arr, target))


if __name__ == '__main__':
    main()

"""
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.


Constraints:

3 <= mountain_arr.length() <= 104
0 <= target <= 109
0 <= mountain_arr.get(index) <= 109

"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (mid == n - 1 and mountain_arr.get(n - 2) < mountain_arr.get(n - 1)) or (
                    mid != n - 1 and mountain_arr.get(mid) > mountain_arr.get(mid + 1)):
                right = mid - 1
            else:
                left = mid + 1
        peak = left

        left = 0
        right = peak
        while left <= right:
            mid = left + (right - left) // 2
            x = mountain_arr.get(mid)
            if x >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left <= peak and mountain_arr.get(left) == target:
            return left

        left = peak
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            x = mountain_arr.get(mid)
            if x <= target:
                right = mid - 1
            else:
                left = mid + 1
        if left <= n - 1 and mountain_arr.get(left) == target:
            return left

        return -1


def main():
    array = [1, 2, 3, 4, 5, 3, 1]
    target = 3
    print(Solution().findInMountainArray(target, array))


if __name__ == '__main__':
    main()

"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.


Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def rems(arr: List[int]):
            for num in arr:
                yield num % 2

        cnt = 0
        for rem in rems(arr):
            if rem == 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False


def main():
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(Solution().threeConsecutiveOdds(arr))


if __name__ == '__main__':
    main()

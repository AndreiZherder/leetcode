"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]


Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = 1001
        d = {num: i for i, num in enumerate(arr2)}
        n1, n2 = 0, 0
        for num in arr1:
            if num in d:
                n1 += 1
            else:
                n2 += 1

        ans1 = [0 for i in range(n1)]
        ans2 = [0 for i in range(n2)]
        cnt1 = [0 for i in range(k)]
        cnt2 = [0 for i in range(k)]

        for num in arr1:
            if num in d:
                cnt1[d[num]] += 1
            else:
                cnt2[num] += 1

        for i in range(1, k):
            cnt1[i] += cnt1[i - 1]
            cnt2[i] += cnt2[i - 1]

        for num in reversed(arr1):
            if num in d:
                cnt1[d[num]] -= 1
                ans1[cnt1[d[num]]] = num
            else:
                cnt2[num] -= 1
                ans2[cnt2[num]] = num

        return ans1 + ans2


def main():
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(Solution().relativeSortArray(arr1, arr2))


if __name__ == '__main__':
    main()

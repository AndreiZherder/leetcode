"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.



Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""
from itertools import accumulate
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        pref = list(accumulate(height, max))
        suf = list(accumulate(height[::-1], max))[::-1]
        ans = 0
        for h, p, s in zip(height, pref, suf):
            ans += min(p, s) - h
        return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))


if __name__ == '__main__':
    main()

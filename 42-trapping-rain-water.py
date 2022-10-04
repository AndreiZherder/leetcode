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

from typing import List
from sortedcontainers import SortedSet


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        peaks = []
        indexes = SortedSet()
        up = True
        prev = -float('Inf')
        for i in range(n):
            if up:
                if height[i] >= prev:
                    prev = height[i]
                    continue
                peaks.append((i - 1, height[i - 1]))
                indexes.add(i - 1)
                prev = height[i]
                up = False
            else:
                if height[i] <= prev:
                    prev = height[i]
                    continue
                prev = height[i]
                up = True
        if up:
            peaks.append((n - 1, height[n - 1]))
            indexes.add(n - 1)
        m = len(peaks)
        if m == 1:
            return 0
        peaks.sort(key=lambda x: (-x[1], x[0]))
        ans = 0
        prev_index = peaks[0][0]
        for index, peak in peaks[1:]:
            if index in indexes:
                if prev_index < index:
                    a = prev_index
                    b = index
                else:
                    a = index
                    b = prev_index
                left = indexes.bisect_left(a)
                right = indexes.bisect_right(b)
                del indexes[left + 1:right - 1]
                if index < prev_index:
                    step = 1
                else:
                    step = -1
                i = index
                while i != prev_index and height[i] <= height[index]:
                    ans += height[index] - height[i]
                    i += step
                prev_index = index
        return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))


if __name__ == '__main__':
    main()

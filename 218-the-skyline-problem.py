"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
when viewed from a distance. Given the locations and heights of all the buildings,
return the skyline formed by these buildings collectively.

The geometric information of each building
is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate
in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment
in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark
the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]



Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings.
The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]


Constraints:

1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 2^31 - 1
buildings is sorted by lefti in non-decreasing order.
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def getSkyline(self, b: List[List[int]]) -> List[List[int]]:
        n = len(b)
        b.sort(key=lambda x: (x[0], -x[2], x[1]))
        max_right = b[0][1]
        for left, right, height in b[1:]:
            max_right = max(max_right, right)
        heap = []
        ans = [[b[0][0], b[0][2]]]
        cur_right = b[0][1]
        cur_height = b[0][2]
        heappush(heap, (-b[0][2], b[0][0], b[0][1]))
        i = 1
        while i < n or heap:
            while i < n and b[i][0] <= cur_right:
                if b[i][2] == cur_height:
                    cur_right = b[i][1]
                if b[i][2] > cur_height:
                    ans.append([b[i][0], b[i][2]])
                    cur_right = b[i][1]
                    cur_height = b[i][2]
                heappush(heap, (-b[i][2], b[i][0], b[i][1]))
                i += 1
            flag = False
            while heap:
                h, left, right = heappop(heap)
                h = -h
                if right > cur_right:
                    if h < cur_height:
                        flag = True
                        break
                    else:
                        cur_right = right
            if flag:
                ans.append([cur_right, h])
                cur_right = right
                cur_height = h
                heappush(heap, (-h, cur_right, cur_right))
            else:
                ans.append([cur_right, 0])
                if i < n:
                    ans.append([b[i][0], b[i][2]])
                    cur_right = b[i][1]
                    cur_height = b[i][2]
                    heappush(heap, (-b[i][2], b[i][0], b[i][1]))
                    i += 1
        if ans[-1] != [max_right, 0]:
            ans.append([max_right, 0])
        return ans


def main():
    # buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    # buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
    # buildings = [[1, 20, 1], [1, 21, 2], [1, 22, 3]]
    # buildings = [[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]]
    # buildings = [[2, 14, 4], [4, 8, 8], [6, 16, 4]]
    buildings = [[4547, 253463, 513907], [16593, 154606, 197418], [20536, 587972, 480271], [25155, 135407, 277021],
                 [45693, 480063, 10484], [57392, 70775, 887782], [69423, 760082, 373899], [93047, 222798, 416217],
                 [105421, 832604, 877583], [113118, 797930, 760771], [128302, 234173, 548113], [137036, 889837, 902341],
                 [151470, 195177, 920702], [153020, 398494, 465441], [153980, 501882, 565647], [159005, 416356, 28559],
                 [218765, 535515, 140331], [303595, 627878, 399999], [333489, 449295, 827098], [359242, 830671, 455392],
                 [390291, 400129, 693584], [429774, 450923, 637981], [493315, 563384, 655884], [500860, 718561, 769319],
                 [507299, 817616, 228], [537517, 989102, 300696], [543853, 843011, 695472], [550404, 559944, 90888],
                 [617555, 907369, 523648], [622624, 989745, 894596], [640808, 867707, 963706], [697210, 716449, 705689],
                 [804555, 914745, 764029]]
    print(Solution().getSkyline(buildings))


if __name__ == '__main__':
    main()

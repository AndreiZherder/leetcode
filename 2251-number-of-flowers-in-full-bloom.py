"""
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in
full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n,
where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the
ith person arrives.



Example 1:
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:
Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.


Constraints:

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= people.length <= 5 * 104
1 <= people[i] <= 109

"""
from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        def index(arr: List[int], num: int) -> int:
            return bisect_right(arr, num) - 1

        s = {-10 ** 20}
        for x1, x2 in flowers:
            s.add(x1)
            s.add(x1 + 1)
            s.add(x2)
            s.add(x2 + 1)
        xs = sorted(s)
        n = len(xs)
        diff = [0 for i in range(n + 1)]
        for x1, x2 in flowers:
            diff[index(xs, x1)] += 1
            diff[index(xs, x2) + 1] -= 1
        a = list(accumulate(diff))
        ans = []
        for x in people:
            ans.append(a[index(xs, x)])
        return ans


def main():
    flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
    people = [2, 3, 7, 11]
    print(Solution().fullBloomFlowers(flowers, people))


if __name__ == '__main__':
    main()

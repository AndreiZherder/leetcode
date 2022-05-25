"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater
than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.



Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1


Constraints:

1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5
"""
from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        return self.lengthOfLIS(y for x, y in sorted(envelopes, key=lambda envelope: (envelope[0], -envelope[1])))

    def lengthOfLIS(self, nums) -> int:
        dp = []
        n = -1
        for num in nums:
            i = bisect_left(dp, num)
            if i > n:
                dp.append(num)
                n += 1
            else:
                dp[i] = num
        return n + 1


def main():
    # envelopes = [[1, 15], [7, 18], [7, 6], [7, 100], [2, 200], [17, 30], [17, 45], [3, 5], [7, 8], [3, 6], [3, 10],
    #              [7, 20], [17, 3], [17, 45]]
    # envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
    print(Solution().maxEnvelopes(envelopes))


if __name__ == '__main__':
    main()

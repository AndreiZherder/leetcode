"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 0
        n = len(ratings)
        ratings = [ratings[0], ratings[0]] + ratings + [ratings[-1], ratings[-1]]
        n += 4
        low1 = 1
        for i in range(2, n - 1):
            if ratings[i - 1] >= ratings[i] and ratings[i + 1] >= ratings[i]:
                low2 = i
                a = low1
                while ratings[a + 1] > ratings[a]:
                    a += 1
                b = low2
                while ratings[b - 1] > ratings[b]:
                    b -= 1
                n1 = a - low1
                n2 = low2 - b
                if a == b:
                    if n1 >= n2:
                        ans += (3 + n1) * n1 // 2
                        ans += (2 + n2) * (n2 - 1) // 2
                    else:
                        ans += (3 + n2) * n2 // 2
                        ans += (2 + n1) * (n1 - 1) // 2
                else:
                    ans += (3 + n1) * n1 // 2
                    ans += (3 + n2) * n2 // 2
                ans += 1
                low1 = low2
        ans -= 1
        return ans


def main():
    # ratings = [1, 0, 2]
    # ratings = [1, 2, 2]
    # ratings = [1]
    # ratings = [1, 1]
    # ratings = [1, 1, 1]
    # ratings = [1, 1, 1, 1]
    # ratings = [1, 2, 1]
    # ratings = [2, 1, 2]
    # ratings = [1, 1, 2]
    # ratings = [2, 2, 1]
    ratings = [2, 1, 2, 3, 4, 1, 2, 2, 1, 0]
    print(Solution().candy(ratings))


if __name__ == '__main__':
    main()

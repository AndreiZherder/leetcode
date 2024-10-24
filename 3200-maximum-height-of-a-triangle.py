"""
You are given two integers red and blue representing the count of red and blue colored balls.
You have to arrange these balls to form a triangle such that the 1st row will have 1 ball,
the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.

All the balls in a particular row should be the same color, and adjacent rows should have different colors.

Return the maximum height of the triangle that can be achieved.



Example 1:

Input: red = 2, blue = 4

Output: 3

Explanation:
Example 2:

Input: red = 2, blue = 1

Output: 2

Explanation:
Example 3:

Input: red = 1, blue = 1

Output: 1

Example 4:

Input: red = 10, blue = 1

Output: 2

Explanation:
Constraints:

1 <= red, blue <= 100
"""


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def solve(red: int, blue: int) -> int:
            balls = [red, blue]
            ans = 0
            cur = 0
            cnt = 1
            while True:
                if balls[cur] - cnt >= 0:
                    ans += 1
                    balls[cur] -= cnt
                    cur ^= 1
                    cnt += 1
                else:
                    return ans

        return max(solve(red, blue), solve(blue, red))


def main():
    red = 2
    blue = 4
    print(Solution().maxHeightOfTriangle(red, blue))


if __name__ == '__main__':
    main()

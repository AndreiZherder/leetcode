"""
You are given two integers n and x. You have to construct an array of positive integers nums of size n
where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i],
and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].



Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.



Constraints:

1 <= n, x <= 108

"""
from typing import List


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        m = 32
        first = bin(x)[2:].zfill(m)
        last = bin(n - 1)[2:].zfill(m)
        ans = []
        i = m - 1
        j = m - 1
        while j >= 0:
            if i >= 0 and first[i] == '1':
                ans.append('1')
                i -= 1
            else:
                ans.append(last[j])
                i -= 1
                j -= 1
        return int(''.join(ans)[::-1], 2)


def main():
    n = 3
    x = 4
    print(Solution().minEnd(n, x))


if __name__ == '__main__':
    main()

"""
You are given a string s and an integer k. You can choose one of the first k letters of s and append it
at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.



Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation:
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation:
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".


Constraints:

1 <= k <= s.length <= 1000
s consist of lowercase English letters.
"""
from collections import deque


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        else:
            n = len(s)
            q = deque(s)
            ans = s
            for i in range(n):
                q.rotate(-1)
                ans = min(ans, ''.join(q))
            return ans


def main():
    s = "baaca"
    k = 3
    print(Solution().orderlyQueue(s, k))


if __name__ == '__main__':
    main()

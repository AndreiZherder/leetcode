"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size.
Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
indicates that the person labeled ai does not like the person labeled bi,
return true if it is possible to split everyone into two groups in this way.



Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 10^4
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        s = [set(), set()]
        g = defaultdict(list)
        for v, u in dislikes:
            g[v].append(u)
            g[u].append(v)
        for node in g:
            if node in s[0] or node in s[1]:
                continue
            part = 0
            q1, q2 = deque([node]), deque()
            s[part].add(node)
            while q1:
                while q1:
                    v = q1.popleft()
                    for u in g[v]:
                        if u in s[part]:
                            return False
                        if u not in s[part ^ 1]:
                            s[part ^ 1].add(u)
                            q2.append(u)
                q1, q2 = q2, q1
                part ^= 1
        return True


def main():
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(Solution().possibleBipartition(n, dislikes))


if __name__ == '__main__':
    main()

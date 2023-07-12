"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from typing import List


class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(v: int) -> bool:
            for u in g[v]:
                if color[u] == GREY:
                    return False
                elif color[u] == WHITE:
                    color[u] = GREY
                    if not dfs(u):
                        return False
                    color[u] = BLACK
            ans.append(v)
            return True

        WHITE = 0
        GREY = 1
        BLACK = 2
        g = [[] for v in range(n)]
        color = [WHITE for v in range(n)]
        for v, u in edges:
            g[u].append(v)
        ans = []
        for v in range(n):
            if color[v] == WHITE:
                color[v] = GREY
                if not dfs(v):
                    return []
                color[v] = BLACK
        return ans[::-1]


def main():
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().findOrder(numCourses, prerequisites))


if __name__ == '__main__':
    main()

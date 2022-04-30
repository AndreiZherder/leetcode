"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi]
and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj]
represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid.
You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import deque
from typing import List


class Node:
    def __init__(self, s: str):
        self.united_with = s
        self.rank = 0
        self.children = []


class Solution:
    def __init__(self):
        self.nodes = dict()

    def find(self, s: str) -> str:
        while s != self.nodes[s].united_with:
            s = self.nodes[s].united_with
        return s

    def union(self, s1: str, s2: str):
        id1 = self.find(s1)
        id2 = self.find(s2)
        if id1 != id2:
            if self.nodes[id1].rank > self.nodes[id2].rank:
                self.nodes[id2].united_with = id1
            else:
                self.nodes[id1].united_with = id2
                if self.nodes[id1].rank == self.nodes[id2].rank:
                    self.nodes[id2].rank += 1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        for equation, value in zip(equations, values):
            var1, var2 = equation
            if var1 not in self.nodes:
                self.nodes[var1] = Node(var1)
            if var2 not in self.nodes:
                self.nodes[var2] = Node(var2)
            self.nodes[var1].children.append((var2, value))
            self.nodes[var2].children.append((var1, 1 / value))
            self.union(var1, var2)
        ans = []
        for var1, var2 in queries:
            if var1 not in self.nodes or var2 not in self.nodes:
                ans.append(-1)
                continue
            if self.find(var1) != self.find(var2):
                ans.append(-1)
                continue
            if var1 == var2:
                ans.append(1)
                continue
            q = deque([(var1, 1)])
            visited = {var1}
            while q:
                var1, acc = q.popleft()
                children = self.nodes[var1].children
                for var, mul in children:
                    if var not in visited:
                        if var == var2:
                            ans.append(acc * mul)
                            q.clear()
                            break
                        q.append((var, acc * mul))
                        visited.add(var)
        return ans


def main():
    equations = [["a", "b"], ["b", "c"], ["a", "c"]]
    values = [2.0, 3.0, 6.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calcEquation(equations, values, queries))


if __name__ == '__main__':
    main()

"""
You are given an array of strings equations that represent relationships between variables where each string
equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here,
xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations,
or false otherwise.



Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""
from typing import List


class Node:
    def __init__(self, parent: int):
        self.parent = parent
        self.rank = 0


class DSU:
    def __init__(self):
        self.nodes = [Node(i) for i in range(26)]

    def find(self, i: int) -> int:
        while i != self.nodes[i].parent:
            i = self.nodes[i].parent
        return i

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.nodes[id1].rank > self.nodes[id2].rank:
            self.nodes[id2].parent = id1
        else:
            self.nodes[id1].parent = id2
            if self.nodes[id1].rank == self.nodes[id2].rank:
                self.nodes[id2].rank += 1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        orda = ord('a')
        dsu = DSU()
        notequal = []
        for e in equations:
            if e[1] == '!':
                notequal.append((ord(e[0]) - orda, ord(e[3]) - orda))
            else:
                dsu.union(ord(e[0]) - orda, ord(e[3]) - orda)
        for i, j in notequal:
            if dsu.find(i) == dsu.find(j):
                return False
        return True


def main():
    equations = ["a==b","b!=a"]
    print(Solution().equationsPossible(equations))


if __name__ == '__main__':
    main()

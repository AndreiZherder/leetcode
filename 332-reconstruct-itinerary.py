"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



Example 1:

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi

"""
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for v, u in tickets:
            g[v].append(u)
        for v in g:
            g[v].sort(reverse=True)

        # Hierholzer's Algorithm for Euler Path/Circuit
        # https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
        # Maintain a stack to keep vertices
        # here we start with 'JFK'
        path = ['JFK']

        # list to store final circuit
        ans = []

        while path:
            v = path[-1]

            # If there's remaining edge in adjacency list
            # of the current vertex
            if g[v]:

                # Find and remove the next vertex that is
                # adjacent to the current vertex
                u = g[v].pop()

                # Push the new vertex to the stack
                path.append(u)

            # back-track to find remaining circuit
            else:
                # Remove the current vertex and
                # put it in the circuit
                ans.append(path.pop())

        return ans[::-1]


def main():
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(Solution().findItinerary(tickets))


if __name__ == '__main__':
    main()

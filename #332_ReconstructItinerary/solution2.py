# Method: Use hashmap to store map of src and dest list,
# then use DFS (iterative) to calculate the itinerary
# TC: O(nlogn)
# SC: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)

        itinerary = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())
        return itinerary[::-1]

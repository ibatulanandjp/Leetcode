# Method: Use hashmap to store map of src and dest list,
# then use DFS (recursive) to calculate the itinerary
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

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]

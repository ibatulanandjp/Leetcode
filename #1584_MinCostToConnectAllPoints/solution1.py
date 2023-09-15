# Method: Use Prims algorithm to calculate Minimum Spanning Tree, and return the weight
# TC: O(n^2 logn), due to priority queue operations
# SC: O(n), for storing the priority queue and visited nodes
from typing import List
from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n

        heap_dict = {0: 0}  # Dictionary with {point_index: distance}
        min_heap = [(0, 0)]  # Priority Queue with [(weight, point_index)]

        mst_weight = 0

        while min_heap:
            w, u = heappop(min_heap)

            if visited[u] or heap_dict.get(u, float('inf')) < w:
                continue

            visited[u] = True
            mst_weight += w

            for v in range(n):
                if not visited[v]:
                    new_distance = abs(
                        points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])

                    if new_distance < heap_dict.get(v, float('inf')):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))

        return mst_weight

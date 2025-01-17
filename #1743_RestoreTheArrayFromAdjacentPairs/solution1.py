# Method: Use Hashmap (Graph) and DFS to find the next node within the graph starting from root
# TC: O(n)
# SC: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node, ans)

        ans = []
        dfs(root, None, ans)
        return ans
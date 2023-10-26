# Method: Use DP with finding factors and then calculating combinations of factors
# TC: O(n^2)
# SC: O(n)
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        node_map = {node: 1 for node in arr}
        for node in arr:
            for factor in arr:
                if factor == node:
                    break
                if node % factor == 0 and node // factor in node_map:
                    node_map[node] += node_map[factor] * \
                        node_map[node // factor]
        return sum(node_map.values()) % MOD

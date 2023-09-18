# Method: Use hashmap to count 1s and then sort by count, and return top k indices
# TC: O(m*logm), for sorting array of length m
# SC: O(m), where m is no. of rows
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count_map = {}
        for i, row in enumerate(mat):
            count_map[i] = 0
            for num in row:
                if num:
                    count_map[i] += 1
                else:
                    break
        res = sorted(count_map, key=count_map.get)
        return res[:k]

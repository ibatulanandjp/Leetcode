# Method: Create tuples (count, row_index) and sort it, to return top k elements
# TC: O(m logm), for sorting array of length m
# SC: O(m), where m is no. of rows
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = [(sum(row), i) for i, row in enumerate(mat)]
        row_strength.sort(key=lambda x: (x[0], x[1]))
        return [row[1] for row in row_strength[:k]]

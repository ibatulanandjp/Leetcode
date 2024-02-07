# Method: Use HashMap to count frequency, 
# and then priority queue (max heap) to sort the entries, 
# and return by building a string out of it
# TC: O(n logn)
# SC: O(n)
from collections import defaultdict
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = defaultdict(int)
        for ch in s:
            freq_map[ch] += 1
        
        pq = [(-freq, ch) for ch, freq in freq_map.items()]
        heapq.heapify(pq)

        result = ""
        while pq:
            freq, ch = heapq.heappop(pq)
            result += ch * -freq
        return result        
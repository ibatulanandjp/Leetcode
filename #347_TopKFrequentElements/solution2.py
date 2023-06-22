# Method: Using Hashmap and Max Heap
# TC: O(klogn)
# SC: O(n)
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create count hashmap
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Create max heap (with -ve value, since minheap is the default)
        heap = []
        for key, val in count.items():
            heap.append((-val, key))
        heapq.heapify(heap)

        # Find the top k elements with heappop
        res = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)

        return res
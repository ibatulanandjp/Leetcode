# Method: Heap
# TC: O(n + klogn), heapify + heappop 
# SC: O(n), for heap
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert nums into heap (nagative value to create maxHeap): default: min-heap
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1

        # Return -ve of first element from the maxHeap
        return -maxHeap[0]

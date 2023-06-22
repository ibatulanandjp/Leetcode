# Method: Using HashMap and Bucket Sort
# TC: O(n), since bucket sort is done with bucket-key as count, and bucket-value as list of nums with that many count
# SC: O(n), for hashmap
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Create hashmap with existing count+1, else 0 as default value 
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Create the count freq list [0, 1, 2, ... n]
        for n, c in count.items():
            freq[c].append(n)

        # Solve with bucket sort
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
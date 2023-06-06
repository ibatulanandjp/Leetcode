# Method: Brute-force (Naive)
# TC: O(nlogn)
# SC: O(1) -> O(n), in case the sort() function uses O(n) space
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        return sorted(nums)[len(nums)-k]

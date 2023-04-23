# Using Hashmap with optimization
# TC: O(M+N)
# SC: O(min(M, N))
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Swap nums1 and nums2, with the smallest size as 1st parameter, if needed
        if len(nums1) < len(nums2):
            self.intersect(nums2, nums1)

        # Create count of all elements occurence in the list nums2 (larger list)
        cnt = Counter(nums2)
        result = []

        # Iterate over the shorter list
        for num in nums1:
            # If the count of that element is greater than 0
            if cnt[num] > 0:
                result.append(num)
                cnt[num] -= 1
        return result


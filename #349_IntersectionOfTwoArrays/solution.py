# Method: Use 1 Hashmap to track intersection
# TC: O(n+m)
# SC: O(n+m)
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_dict = {}
        result = []

        for n in nums1:
            nums_dict[n] = 1

        for n in nums2:
            if n in nums_dict and nums_dict[n] == 1:
                nums_dict[n] += 1
                result.append(n)

        return result

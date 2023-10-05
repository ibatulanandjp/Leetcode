# Method: Use Hashmap to count the occurrence of each number, and return a list of ones with greater than n/3
# TC: O(n)
# SC: O(n)
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_map = Counter(nums)

        res = []
        for key, val in count_map.items():
            if val > n//3:
                res.append(key)
        return res

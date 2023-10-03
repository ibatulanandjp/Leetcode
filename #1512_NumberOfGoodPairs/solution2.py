# Method: Use hashmap to count the pairs
# TC: O(n), where n is the length of nums
# SC: O(1)
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count_map = {}

        for num in nums:
            if num in count_map:
                res += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1
        return res

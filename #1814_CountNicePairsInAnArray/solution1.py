# Method: Replace each element with (num + rev(num)) and then Use Hashmap to count frequency
# TC: O(n)
# SC: O(n) 
from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        res = 0
        MOD = 10 ** 9 + 7
        for i in range(len(nums)):
            nums[i] = nums[i] - self.rev(nums[i])
            res = (res + freq_map[nums[i]]) % MOD
            freq_map[nums[i]] += 1
        return res
    
    def rev(self, num: int) -> int:
        res = 0
        while num:
            res = res * 10 + num % 10
            num //= 10
        return res
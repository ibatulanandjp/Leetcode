# Method: 
# Use HashSet and find the fist number of each sequence
# and if it is the first number, start counting the length of the sequence
# Keep track of the longest sequence found
# TC: O(n), where n is the number of elements in nums
# SC: O(1)
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
# Method: Moore Voting Algorithm (Based on the fact that majority element will always be greater than n/2)
# If the num is same as candidate, increment it
# else, decrement it
# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

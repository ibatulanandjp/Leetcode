# Method: Generate set of all strings for the given length, and find the one which doesn't exist
# TC: O(n^2), since we iterate over n numbers, then convert it to string when answer is found 
# SC: O(n), since we use set of integers
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans

        return ""

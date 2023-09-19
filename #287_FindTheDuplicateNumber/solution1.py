# Method: Use Binary Search to compare the mid with count less than mid
# If greater, search on the left, else on the right
# TC: O(n*logn), due to binary search combined with array scanning
# SC: O(1)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low

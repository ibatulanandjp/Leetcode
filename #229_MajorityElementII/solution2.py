# Method: Use Boyer-Moore Voting Algorithm to find the top 2 candidates, 
# and iterate over the list again to count the occurrence of these candidates to be greater than n/3
# TC: O(n), where n is the length of list nums
# SC: O(1)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [num for num in (candidate1, candidate2) if nums.count(num) > len(nums)//3]

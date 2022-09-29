import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return[self.firstIndex(nums, target), self.lastIndex(nums, target)]
    
    def firstIndex(self, nums: List[int], target: int) -> int:
        index=-1
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = math.floor(low + (high-low)/2)
            if nums[mid] == target:
                index = mid
                high = mid-1
                
            elif nums[mid] > target:
                high = mid-1
                
            else:
                low = mid+1
                
        return index
    
    def lastIndex(self, nums: List[int], target: int) -> int:
        index=-1
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = math.floor(low + (high-low)/2)
            if nums[mid] == target:
                index = mid
                low = mid+1
                
            elif nums[mid] > target:
                high = mid-1
                
            else:
                low = mid+1
                
        return index
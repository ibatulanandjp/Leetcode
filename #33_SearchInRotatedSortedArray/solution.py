from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums)-1
        
        # Find the pivot index 
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        pivot = low

        # Find the index of target
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            realmid = (mid+pivot)%len(nums)
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                low = mid+1
            else:
                high = mid-1
            
        return -1
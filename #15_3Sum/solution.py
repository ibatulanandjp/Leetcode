from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        # For the 1st element in the triplet
        for i in range(len(nums)):    
            triplet = []
            
            seen_map = {}
            # For the 2nd and 3rd elements in the triplet [Two Sum Problem #1]
            for j in range(i, len(nums)):
                remaining = 0 - (nums[i] + nums[j])
                    
                # If the 3rd element is in seen map and indexes are different
                if remaining in seen_map and i!=j and j!=seen_map[remaining] and i!=seen_map[remaining]:
                    triplet = [nums[i], nums[j], remaining]

                    # If the triplet is unique
                    if triplet not in res:
                        res.append(triplet)
                
                # Add the 3rd num "value: index" to the map
                seen_map[nums[j]] = j
                        
        return res

sol = Solution()
res = sol.threeSum([-1,0,1,2,-1,-4])
print(res)
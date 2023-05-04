from typing import List


# Method: Backtracking (Iterative) Top-to-bottom
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        permutation = []
        
        # Initiate the stack with all the numbers in the list
        for i in nums:
            stack.append([i])
        
        while stack:
            curr_nums = stack.pop()
            
            # Base Case
            if len(curr_nums) == len(nums):
                permutation.append(curr_nums)
                
            for n in nums:
                if n not in curr_nums:
                    temp = curr_nums[:] # Deep copy is "IMPORTANT"
                    temp.append(n)
                    stack.append(temp)

        return permutation
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump = [0 for i in nums]
        m_index = 0
        
        for i in range(len(nums)): 
            # Return true if last element can be reached
            if m_index >= len(nums)-1:
                return True
            
            # Return false if current index can't be reached
            if m_index < i:
                return False
            
            # Update the max_jump list and m_index
            max_jump[i] = max(m_index, i+nums[i])
            m_index = max(m_index, max_jump[i])
    
        return False
                
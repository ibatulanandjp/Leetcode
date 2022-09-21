class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        
        for i in range(len(s)):
            # Even case
            s1 = self.expandAroundCenter(s, i, i)
            if len(s1) > len(res):
                res = s1
            
            # Odd case
            s2 = self.expandAroundCenter(s, i, i+1)            
            if len(s2) > len(res):
                res = s2
                   
        return res
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        if s=="" or left>right: return 0
        
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
            
        return s[left+1:right]
        
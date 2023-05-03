class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Set to maintain the characters newly found in the sliding window
        charSet = set()
        maxLength = 0
        
        # Left bound of sliding window
        l = 0
        
        for r in range(len(s)):
            # Until we remove the right element duplicate from the window,
            # Remove the left bound element and Move left by 1
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Add the right element if it's unique
            charSet.add(s[r])
            # Update the maxLength
            maxLength = max(maxLength, r-l+1)
            
        return maxLength
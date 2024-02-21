# Method: Use AND of number and a number less to check if it is a power of 2
# TC: O(1)
# SC: O(1) 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0
# Method: Use recursion
# Pattern for recursion - length(nth row) = 2 * length(n-1th row) 
# and if k is in the 1st half, then k at nth row is same as n-1th row
# and if k is in the 2nd half, then k at nth row is same as k - length(n-1th row) 
# TC: O(n)
# SC: O(n)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # Length of bits in nth row (2^(n-2)), since n is 1-indexed
        length = 2 ** ((n - 1) - 1)
        # If kth element is in First half
        if k <= length:
            return self.kthGrammar(n-1, k)
        # If kth element is in Second half
        else:
            return 1 - self.kthGrammar(n-1, k-length)

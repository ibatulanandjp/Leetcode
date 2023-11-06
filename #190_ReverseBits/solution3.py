# Method: Use Bit manipulation to left shift the result and add the last bit, then right shift the num
# TC: O(1)
# SC: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # Left Shift the result by 1
            # If the last bit is 1, add 1
            res = (res<<1) + (n&1)
            # Right Shift the number by 1
            n>>=1
        return res
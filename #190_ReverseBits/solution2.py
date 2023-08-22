class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Left Shift the result by 1
            res = res << 1
            # If the last bit is 1, add 1
            if n & 1 == 1:
                res += 1
            # Right Shift the number by 1
            n >>= 1
        return res

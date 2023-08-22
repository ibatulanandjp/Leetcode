# Method: Using General Mathematics

class Solution:
    def reverseBits(self, n: int) -> int:
        rev_bits = ""
        while n >= 1:
            rev_bits += str(n % 2)
            n //= 2
        while len(rev_bits) < 32:
            rev_bits += "0"

        res = 0
        for i in range(32):
            res += 2**i * int(rev_bits[31-i])

        return res

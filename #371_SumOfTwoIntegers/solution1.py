# Method: Bit manipulation - Use AND for carry, XOR for sum
# TC: O(1)
# SC: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32bit mask in hexadecimal 
        # To prevent overflow, we use 32bit mask to limit int size to 32bit
        mask = 0xffffffff
        while (b & mask > 0):
            # Calculate carry with AND and left shift
            carry = (a & b) << 1
            # Calculate sum with XOR
            a = a ^ b
            b = carry
        return (a & mask) if b>0 else a
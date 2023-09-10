# Method: Using XOR to find the number of set bits (1s)
# TC: O(n), where n is the number of bits of the given numbers (in this case, n=32)
# SC: O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Calculate XOR of x and y
        value = x ^ y

        # Calculate no. of '1' bits in the XOR value
        distance = 0
        while value > 0:
            distance += value % 2
            value //= 2
        return distance

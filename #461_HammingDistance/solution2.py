# Method: Using Brian-Kernighan and XOR to find the number of set bits (1s)
# TC: O(k), where k is the hamming distance between given numbers
# SC: O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Calculate XOR of x and y
        value = x ^ y

        # Calculate no. of '1' bits in the XOR value
        distance = 0
        while value > 0:
            distance += 1
            # Update value to unset the rightmost bit (Brian-Kernighan "n & (n-1)" rule)
            value = value & (value-1)
        return distance

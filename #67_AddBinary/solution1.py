# Method: Binary to Integer conversion and addition
# TC: O(n+m)
# SC: O(n+m)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = self.btoi(a)
        num_b = self.btoi(b)

        res = self.itob(num_a + num_b)
        return res if res else "0"
    
    # Function to convert binary string to integer
    def btoi(self, binary: str) -> int:
        num = 0
        binary = binary[::-1]
        for i in range(len(binary)):
            num += 2**i * int(binary[i])
        return num

    # Function to convert integer to binary string
    def itob(self, num: int) -> str:
        res = ""
        while num>0:
            res = str(num%2) + res
            num //= 2
        return res
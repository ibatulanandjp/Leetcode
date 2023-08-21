# Method: Using basic mathematics

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >= 1:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

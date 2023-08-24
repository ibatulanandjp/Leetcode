# Method: Store the seen numbers in a set to find the looping values
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            n = self.squaredSum(n)
        return n == 1

    def squaredSum(self, n: int) -> int:
        total = 0
        while n > 0:
            total += (n % 10) ** 2
            n //= 10
        return total

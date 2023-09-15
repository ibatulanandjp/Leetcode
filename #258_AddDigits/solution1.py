# Method: Iteratively calculate the sum
# TC: O(ceil(log10(n))^2) - for iteration over digits recursively
# SC: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 > 0:
            res = 0
            while num:
                res += num % 10
                num //= 10
            num = res
        return num

# Method: Iterate till the int size and check for the number
# TC: O(1)
# SC: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            res = 2 ** i
            if res == n:
                return True
        return False
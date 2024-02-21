# Method: Right shift both numbers and count until they are same, and then left shift it count times
# TC: O(log n)
# SC: O(1)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count

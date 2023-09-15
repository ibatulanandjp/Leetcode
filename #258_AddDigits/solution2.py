# Method: Digit Root method - Use divisibility by 9 (Math)
# TC: O(1)
# SC: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

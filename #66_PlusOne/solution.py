from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Set initial carry to 1, since we have to add "1" to the number
        carry = 1

        # For every number in the reversed order
        for i in range(len(digits)-1, -1, -1):
            added = digits[i] + carry
            digits[i] = added % 10
            carry = 1 if added > 9 else 0

        # Return with [1] appended in the beginning if carry is 1, else simply return 
        return ([1] + digits) if carry == 1 else digits

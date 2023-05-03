from typing import List

# Method: Set 1st and 2nd value to integer_max and find the increasing triplet in 1 pass
# TC: O(n)
# SC: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')

        for n in nums:
            if first >= n:
                first = n
            elif second >= n:
                second = n
            else:
                return True
        return False

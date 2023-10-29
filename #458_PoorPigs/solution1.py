# Method: Use Math calculate the min. no. of pigs using the formula
# upto buckets = (minutesToTest / minutesToDie + 1) ^ pigs
# TC: O(log n), where n is the number of buckets
# SC: O(1)
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        maxTime = minutesToTest / minutesToDie + 1
        pigs = 0
        while maxTime ** pigs < buckets:
            pigs += 1
        return pigs

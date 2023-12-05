# Method: For n teams, there must be n-1 eliminated for 1 to be winner
# TC: O(1)
# SC: O(1)
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1

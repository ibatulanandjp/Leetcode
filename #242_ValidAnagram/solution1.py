# Approach: Sorting
# TC: O(n log n + m log m), where n is the length of s and m is the length of t
# SC: O(n + m) for the sorted lists
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

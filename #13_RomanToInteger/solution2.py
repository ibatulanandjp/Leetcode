# Method: If the previous letter's value is less than current, it's always subtracted, else added
# TC: O(n), where n is the length of the string
# SC: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        ri_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        prev = 0

        for i in range(len(s)-1, -1, -1):
            curr = ri_map[s[i]]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr
        return res

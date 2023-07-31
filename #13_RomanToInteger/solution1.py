# Method: Handle the special cases of subtracting
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

        for i in range(len(s)-1, -1, -1):
            if (
                    (i != len(s)-1) and
                    (
                        (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or
                        (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or
                        (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"))
                    )):
                res -= ri_map[s[i]]
            else:
                res += ri_map[s[i]]
        return res

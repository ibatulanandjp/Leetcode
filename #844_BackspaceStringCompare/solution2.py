# Method: Use Two-pointers to build effective string and compare them
# TC: O(n)
# SC: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # Function to build effective string using 2 pointers
        def buildString(string):
            j = 0
            for i in range(len(string)):
                if string[i] != "#":
                    string[j] = string[i]
                    j += 1
                else:
                    if j > 0:
                        j -= 1
            return j

        # Convert strings to lists for in-place modifications
        s, t = list(s), list(t)
        # Build the string to prepare effective string with length
        p = buildString(s)
        q = buildString(t)

        # If effective lengths are different, return False
        if p != q:
            return False

        # Compare the effective string
        for i in range(p):
            if s[i] != t[i]:
                return False
        return True

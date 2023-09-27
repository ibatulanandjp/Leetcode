# Method: Use array to store index, and then go reverse, calculating the mod with k to return the character
# TC: O(n), where n is the length of the string
# SC: O(n)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        lens = [0]

        for ch in s:
            if ch.isalpha():
                lens.append(lens[-1] + 1)
            else:
                lens.append(lens[-1] * int(ch))

        for i in range(len(s), 0, -1):
            k %= lens[i]
            if k == 0 and s[i-1].isalpha():
                return s[i-1]

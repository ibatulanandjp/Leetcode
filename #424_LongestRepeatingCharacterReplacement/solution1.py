# Method: Use Sliding Window and HashMap to count character frequencies
# Maintain the maximum frequeency of characters in the current window
# TC: O(n), where n is the length of the string
# SC: O(1), since the character set is limited to uppercase English letters
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_map = {}

        l = 0
        # max_freq keeps track of the maximum frequency of any character in the current window
        max_freq = 0
        for r in range(len(s)):
            # If the character is not in the map, update its count
            char_map[s[r]] = char_map.get(s[r], 0) + 1
            max_freq = max(max_freq, char_map[s[r]])

            # If the number of characters that need to be replaced exceeds k,
            # shrink the window from the left until it is valid again
            while max_freq + k < (r - l + 1):
                char_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) 

        return res

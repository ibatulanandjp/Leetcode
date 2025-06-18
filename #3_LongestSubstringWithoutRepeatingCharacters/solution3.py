# Method: Sliding Window with Set (simplified approach for solution 2)
# TC: O(n), where n is the length of the string s
# SC: O(m), where m is the size of the character set (e.g., 26 for lowercase English letters)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        charset = set()

        l = 0
        for r in range(len(s)):
            # Add the unique character at the right pointer
            if s[r] not in charset:
                charset.add(s[r])
                max_length = max(max_length, r-l+1)
            # Remove characters from the left pointer until we remove the duplicate
            else:
                while s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                l += 1
        return max_length
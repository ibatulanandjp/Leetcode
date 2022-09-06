from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


sol = Solution()
res = sol.isAnagram("anagram", "nagarams")
print(res)

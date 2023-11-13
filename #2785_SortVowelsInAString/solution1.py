# Method: Sort the vowels and write back to result
# TC: O(n logn)
# SC: O(n)
class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        vowel_occurrence = []
        for ch in s:
            if ch in vowel_list:
                vowel_occurrence.append(ch)

        vowel_occurrence.sort()
        res = ""
        j = 0
        for i in range(len(s)):
            if s[i] in vowel_list:
                res += vowel_occurrence[j]
                j += 1
            else:
                res += s[i]
        return res
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        # Get both the words' chars until the shortest length word
        n = min(len(word1), len(word2))
        for i in range(n):
            res += word1[i] + word2[i]

        # Append the remaining chars from the string (It will append only from the longest string)
        res += word1[i+1:] + word2[i+1:]
        return res
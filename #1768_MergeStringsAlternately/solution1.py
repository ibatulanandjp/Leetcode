class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i, j, k = 0, 0, 0

        while k < len(word1) + len(word2):
            isOdd = k % 2

            if isOdd:
                res += word2[j]
                j += 1
            else:
                res += word1[i]
                i += 1
            k += 1

            if i == len(word1):
                for ch in word2[j:]:
                    res += ch
                    k += 1
            elif j == len(word2):
                for ch in word1[i:]:
                    res += ch
                    k += 1
        return res

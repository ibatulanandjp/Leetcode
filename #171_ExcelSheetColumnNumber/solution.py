class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, pos = 0, 0
        for ch in reversed(columnTitle):
            res += 26**pos * (ord(ch) - 64)
            pos += 1
        return res

class Solution:
    def myAtoi(self, s: str) -> int:
        sym = 1
        numFound, symFound = False, False
        num = ""

        for i in range(len(s)):
            if s[i] == " ":
                if numFound or symFound:
                    break
                else:
                    continue
            elif s[i] == "-" or s[i] == "+":
                if not symFound and not numFound:
                    symFound = True
                    sym = -1 if s[i] == "-" else 1
                else:
                    break
            elif not s[i].isdigit():
                break
            else:
                numFound = True
                num += s[i]

        if num:
            res = sym * int(num)
            if res.bit_length() >= 32:
                return -pow(2, 31) if sym < 0 else pow(2, 31) - 1
            else:
                return res
        return 0

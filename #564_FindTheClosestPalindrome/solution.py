# Method: Calculate firsthalf, and Create candidates list, then pick the nearest palindromic number from the candidates
# TC: O(1)
# SC: O(1), since the candidates list contains max of 5 elements
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        res = ""

        # For different digits count, i.e. 9...9 and 10...01
        candidates = [str(10**(l-1)-1), str(10**l+1)]
        # print(candidates) # n='123' --> ['99', '1001']

        # Take out the first half part of the number (fixed part)
        prefix = int(n[:(l+1)//2])
        # print(prefix) # 12

        # Create all the possible candidates (palindrome) for the given number
        for firsthalf in map(str, (prefix-1, prefix, prefix+1)):
            if l % 2 == 1:
                secondhalf = firsthalf[:-1]
            else:
                secondhalf = firsthalf
            candidates.append(firsthalf + secondhalf[::-1])
        # print(candidates) # ['99', '1001', '111', '121', '131']

        # Pick the nearest palindromic number from the candidates
        for cand in candidates:
            if cand != n:
                if (res == "" or
                        abs(int(n)-int(cand)) < abs(int(n)-int(res)) or
                        (abs(int(n)-int(cand)) == abs(int(n)-int(res)) and
                         int(cand) < int(res))
                    ):
                    res = cand

        return res

# Method: Use Dynamic Programming (Space optimized bottom up approach)
# TC: O(n)
# SC: O(1)
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        zero, one, two = 0, 0, 1

        for thing in corridor:
            if thing == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD
        return zero
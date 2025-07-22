# Method: Dynamic Programming (bottom-up approach) with tabulation/memoization
# TC: O(n), where n is the number of steps
# SC: O(n), where n is the number of steps (for storing results)
class Solution:
    def climbStairs(self, n: int) -> int:
        fact = [1, 2]
        for i in range(2, n+1):
            fact.append(fact[i-1] + fact[i-2])
        return fact[n-1]

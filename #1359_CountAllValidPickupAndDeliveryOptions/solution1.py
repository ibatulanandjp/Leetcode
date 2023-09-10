# Method: Dynamic Programming, and maths to count combination
# TC: O(n)
# SC: O(1)
class Solution:
    def countOrders(self, n: int) -> int:
        # Base case, when count is 1 for n=1
        count = 1
        for i in range(2, n+1):
            # For a pickup, we have (2i-1) choices
            # For its delivery, we have i choices
            count = (count * (2*i - 1) * i) % (10**9 + 7)
        return count

# Method: Use Dynamic Programming (Optimized) counting the next values following the rules, and returning the total count after n iterations
# TC: O(n), since we iterate through the numbers 1 to n once, updating each vowel in constant time
# SC: O(1), since we use constant space for vowel's count
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        # Initialize each with 1
        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            # Calculate next values for each vowel based on the rules
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a

            # Update the origial values for the next iteration
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        # Return the sum of all vowel counts
        return (a + e + i + o + u) % MOD

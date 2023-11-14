# Method: Create Letter set, find left & right index, and count number of characters in between each letters tuple
# TC: O(n), since we iterate over the string length twice at max
# SC: O(1), since set can't be of length greater than 26
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        res = 0

        for letter in letters:
            left, right = s.index(letter), s.rindex(letter)
            between = set()
            for i in range(left+1, right):
                between.add(s[i]) 
            res += len(between)
        
        return res
# Method: Traverse in reverse order, and whenever the char is an odd number, the largest odd number is found
# TC: O(n)
# SC: O(1)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""
# Method: Single iteration to compare strings
# TC: O(n)
# SC: O(1)
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_dig = '\0'

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                max_dig = max(max_dig, num[i])

        return '' if max_dig == '\0' else max_dig * 3

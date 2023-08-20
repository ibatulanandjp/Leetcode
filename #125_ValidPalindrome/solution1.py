class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        # ASCII: 0-48 A-65 a-97
        nums = [i for i in range(ord("0"), ord("9")+1)]
        upper = [i for i in range(ord("A"), ord("Z")+1)]
        lower = [i for i in range(ord("a"), ord("z")+1)]
        charlist = nums + upper + lower

        while left <= right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif ord(s[left]) not in charlist:
                left += 1
            elif ord(s[right]) not in charlist:
                right -= 1
            else:
                return False

        return True

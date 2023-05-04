from typing import List


# Method: Backtracking (Recursive)
# Store parantheses string in stack and backtrack for (open_count, close_count)
# Recursion Cases:
#   1. Base Case: open_count == close_count == n, add stack to result
#   2. Case 1: open_count < n, add "(" to stack, and backtrack with (open_count+1, close_count)
#   3. Case 2: close_count < n, add ")" to stack, and backtrack with (open_count, close_count+1)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        
        # Function to backtrack and add
        def backtrack(open_count, close_count):
            
            # Base case: open_count == close_count == n
            if open_count == n and close_count == n:
                result.append("".join(stack))
                return
            
            # Case 1: open_count < n
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()
                
            # Case 2: close_count < open_count
            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result
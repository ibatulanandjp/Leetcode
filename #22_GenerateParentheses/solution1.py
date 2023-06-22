from typing import List


# Method: Backtracking (Iterative)
# Store ["parentheses_string", open_count, close_count] on stack
# Cases:
#   1: If open_count==n and close_count==n, then append the parantheses_string to RESULT
#   2: If open_count<n, add parantheses_string+"(" to STACK
#   3: If close_count<open_count, add parantheses_string+")" to STACK
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis_combinations = []
        stack = []

        # Initiate the stack with ["parentheses_string", open_count, close_count]
        stack.append(["(", 1, 0])

        while stack:
            s, open_count, close_count = stack.pop()

            # If the "(" and ")" count has already reached the max (i.e, "n"), add that to result list
            if open_count == n and close_count == n:
                parenthesis_combinations.append(s)

            # If open_count < max, add "(" and increment open_count
            if open_count < n:
                stack.append([s+"(", open_count+1, close_count])

            # If close_count < open_count, add ")" and increment close_count
            if close_count < open_count:
                stack.append([s+")", open_count, close_count+1])

        return parenthesis_combinations

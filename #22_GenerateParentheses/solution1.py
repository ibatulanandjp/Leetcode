from typing import List


# Method: Backtrack Iterative
# Store ["parentheses_string", open_count, close_count] on stack
# 1: If open_count==n and close_count==n, then append the parantheses_string to RESULT
# 2: If close_count<=open_count, 
#       a. if open_count<n, add parantheses_string+"(" to STACK
#       b. if close_count<n, add parantheses_string+")" to STACK
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        parenthesis_combinations = []
        stack = []
        
        # Initiate the stack with ["parentheses_string", open_count, close_count]
        stack.append(["(", 1, 0])
        
        while stack:
            element = stack.pop()
            
            # If the "(" and ")" count has already reached the max (i.e, "n"), add that to result list
            if element[1] ==n and element[2] ==n:
                    parenthesis_combinations.append(element[0])
            
            # If close_count <= open_count
            if element[2] <= element[1]:
                
                # If open_count < max, add "(" and increment open_count
                if element[1] < n:
                    new_element = [(element[0] + "("), element[1]+1, element[2]]
                    stack.append(new_element)
                    
                # If close_count < max, add ")" and increment close_count
                if element[2] < n:
                    new_element = [(element[0] + ")"), element[1], element[2]+1]
                    stack.append(new_element)
            
        return parenthesis_combinations
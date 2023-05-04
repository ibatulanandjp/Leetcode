from typing import List


# Method: Backtrack (Iterative) using stack
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        powerset, stack = [[]], [[]]

        for n in nums:
            stack.append([n])
            powerset.append([n])

        while stack:
            curr_set = stack.pop()

            for n in nums:
                if n not in curr_set:
                    temp = curr_set[:]  # Deep Copy
                    temp.append(n)

                    # Sort the array to avoid duplicates
                    temp = sorted(temp)
                    if temp not in powerset:
                        stack.append(temp)
                        powerset.append(temp)

        return powerset

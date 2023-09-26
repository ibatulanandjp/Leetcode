# Method: Using Greedy approach and Stack
# Maintain seen set and last occurrence of characters
# TC: O(n)
# SC: O(n)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {ch: i for i, ch in enumerate(s)}

        for i, ch in enumerate(s):
            # If character not seen
            if ch not in seen:
                # Remove top character, until it's lesser than stack top and is at lesser index then stack top
                while stack and ch < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                # Add character to stack and seen
                stack.append(ch)
                seen.add(ch)

        return "".join(stack)

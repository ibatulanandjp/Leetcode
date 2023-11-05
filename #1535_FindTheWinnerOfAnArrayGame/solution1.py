# Method: Return max for k greater then arr length, and simulate for the other cases
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # If k is greater than length of arr, max(arr) will be the result
        if k >= len(arr):
            return max(arr)

        curr_winner = arr[0]
        consecutive_wins = 0

        # Iterate through arr, finding the winner with consecutive_wins==k
        for i in range(1, len(arr)):
            if curr_winner > arr[i]:
                consecutive_wins += 1
            else:
                curr_winner = arr[i]
                consecutive_wins = 1
        
            if consecutive_wins == k:
                return curr_winner
            
        return curr_winner
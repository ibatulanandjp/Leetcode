# Method: (Greedy) Use Hashmap to count frequency,
# and then use alphabet array to find the position,
# counting deletions as we move towards left
# TC: O(n)
# SC: O(n)
from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1

        arr = ["" for _ in range(0, len(s)+1)]
        for key, val in freq.items():
            while val > 0 and arr[val] != "":
                val -= 1
                deletions += 1
            arr[val] = key

        return deletions

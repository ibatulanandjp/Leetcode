# Method: (Greedy) Use Hashmap to count frequency,
# and then use frequency set to keep track of freqency used,
# counting deletions as we reduce it
# TC: O(n)
# SC: O(n)
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        freq = Counter(s)

        used_freq = set()
        for char, freq in freq.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                deletions += 1
            used_freq.add(freq)

        return deletions

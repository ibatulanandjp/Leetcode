from cmath import inf
from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        res = []
        prev = [0] * (len(s)+1)
        next = [inf] * (len(s)+1)
        pre_sum = [0] * (len(s)+1)

        for i, ch in enumerate(s):
            pre_sum[i+1] = pre_sum[i] + (ch == "|")
            prev[i+1] = i if ch=="|" else prev[i]

        for i, ch in reversed(list(enumerate(s))):
            next[i] = i if ch=="|" else next[i+1]

        print(prev)
        print(next)
        print(pre_sum)

        for q in queries:
            left = next[q[0]]
            right = prev[q[1]+1]

            res.append(right - left - (pre_sum[right] - pre_sum[left]) if left<right else 0)

        return res